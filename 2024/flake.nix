{
  description = "Advent of code 2024 with OCaml";

  inputs = {
    systems.url = "github:nix-systems/default";
  };

  outputs = { self, nixpkgs, systems }:
    let
      lib = nixpkgs.lib;
      eachSystem = lib.genAttrs (import systems);
    in
    {
      packages = eachSystem (system:
        let
          legacyPackages = nixpkgs.legacyPackages.${system};
          ocamlPackages = legacyPackages.ocamlPackages;
        in
        {
          default = self.packages.${system}.advent_2024;

          advent_2024 = ocamlPackages.buildDunePackage {
            pname = "advent_2024";
            version = "0.1.0";
            duneVersion = "3";
            src = ./.;

            buildInputs = [
              ocamlPackages.core
              ocamlPackages.core_unix
              ocamlPackages.async
              ocamlPackages.ppx_let
              ocamlPackages.ppx_expect
            ];

            strictDeps = true;
          };
        });

      checks = eachSystem (system:
        let
          legacyPackages = nixpkgs.legacyPackages.${system};
          ocamlPackages = legacyPackages.ocamlPackages;
        in
        {
          advent_2024 =
            let
              patchDuneCommand =
                let
                  subcmds = [ "build" "test" "runtest" "install" ];
                in
                lib.replaceStrings
                  (lib.lists.map (subcmd: "dune ${subcmd}") subcmds)
                  (lib.lists.map (subcmd: "dune ${subcmd} --display=short") subcmds);
            in

            self.packages.${system}.advent_2024.overrideAttrs
              (oldAttrs: {
                name = "check-${oldAttrs.name}";
                doCheck = true;
                buildPhase = patchDuneCommand oldAttrs.buildPhase;
                checkPhase = patchDuneCommand oldAttrs.checkPhase;
                # installPhase = patchDuneCommand oldAttrs.checkPhase;
              });

          dune-fmt = legacyPackages.runCommand "check-dune-fmt"
            {
              nativeBuildInputs = [
                ocamlPackages.dune_3
                ocamlPackages.ocaml
                legacyPackages.ocamlformat
              ];
            }
            ''
              echo "checking dune and ocaml formatting"
              dune build \
                --display=short \
                --no-print-directory \
                --root="${./.}" \
                --build-dir="$(pwd)/_build" \
                @fmt
              touch $out
            '';

          nixpkgs-fmt = legacyPackages.runCommand "check-nixpkgs-fmt"
            { nativeBuildInputs = [ legacyPackages.nixpkgs-fmt ]; }
            ''
              echo "checking nix formatting"
              nixpkgs-fmt --check ${./.}
              touch $out
            '';
        });

      devShells = eachSystem (system:
        let
          legacyPackages = nixpkgs.legacyPackages.${system};
          ocamlPackages = legacyPackages.ocamlPackages;
        in
        {
          default = legacyPackages.mkShell {
            packages = [
              legacyPackages.nixpkgs-fmt
              legacyPackages.ocamlformat
              legacyPackages.fswatch
              ocamlPackages.ocaml-lsp
              ocamlPackages.utop
            ];

            inputsFrom = [
              self.packages.${system}.advent_2024
            ];
          };
        });
    };
}
