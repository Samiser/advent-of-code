open! Core
open Async

let label = "3"

module Operation = struct
  type t = Multiply of int * int [@@deriving sexp_of]

  let execute = function Multiply (x, y) -> x * y
end

module Operations = struct
  type t = Operation.t list [@@deriving sexp_of]

  let parse_string s =
    let pattern = Re.Perl.compile_pat "mul\\((\\d+),(\\d+)\\)" in
    Re.all pattern s
    |> List.map ~f:(fun group ->
           let x = Re.Group.get group 1 |> Int.of_string in
           let y = Re.Group.get group 2 |> Int.of_string in
           Operation.Multiply (x, y))

  let remove_disabled_instructions s =
    let pattern =
      Re.Perl.compile_pat
        "do\\(\\)(.|\n)*?don't\\(\\)|^(.|\n)*?don't\\(\\)|do\\(\\)(.|\n)*?$"
    in
    let matches =
      Re.all pattern s |> List.map ~f:(fun group -> Re.Group.get group 0)
    in
    String.concat ~sep:"" matches

  let execute_all t =
    List.map t ~f:(fun operation -> Operation.execute operation)
end

let part_1 input =
  Operations.parse_string input
  |> Operations.execute_all
  |> List.sum (module Int) ~f:Fn.id

let part_2 input = Operations.remove_disabled_instructions input |> part_1

let%expect_test "day 3" =
  let input =
    {|xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))|}
  in
  print_endline (Base_day.solve ~part_1 ~part_2 ~input);
  [%expect {|
    part 1: 161
    part 2: 48
    |}];
  return ()
