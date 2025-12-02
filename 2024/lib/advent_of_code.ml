open! Core
open Async

let day_command (module Day : Day_intf.Day) =
  ( Day.label,
    Command.async_or_error ~summary:[%string "day %{Day.label}"]
      (let%map_open.Command filename =
         anon ("input_file" %: Filename_unix.arg_type)
       in
       fun () ->
         let open Deferred.Or_error.Let_syntax in
         let%bind.Deferred input = Reader.file_contents filename in
         Base_day.solve ~part_1:Day.part_1 ~part_2:Day.part_2 ~input
         |> print_endline;
         return ()) )

let days : (module Day_intf.Day) list =
  [ (module Day_1); (module Day_2); (module Day_3); (module Day_4) ]

let command =
  let commands =
    List.map days ~f:(fun (module Day : Day_intf.Day) ->
        day_command (module Day))
  in
  Command.group ~summary:"advent of code 2024" commands
