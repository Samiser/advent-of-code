open! Core
open Async

let label = "2"

module Report = struct
  type t = int list [@@deriving sexp_of]

  let is_monotonic lst =
    let rec check_increasing = function
      | [] | [ (_ : int) ] -> true
      | x :: y :: rest -> x <= y && check_increasing (y :: rest)
    in
    let rec check_decreasing = function
      | [] | [ (_ : int) ] -> true
      | x :: y :: rest -> x >= y && check_decreasing (y :: rest)
    in
    check_increasing lst || check_decreasing lst

  let differences_within_range lst =
    let rec check_diffs = function
      | [] | [ (_ : int) ] -> true
      | x :: y :: rest ->
          let diff = Int.abs (x - y) in
          (diff >= 1 && diff <= 3) && check_diffs (y :: rest)
    in
    check_diffs lst

  let is_safe t = is_monotonic t && differences_within_range t

  let is_safe_with_dampener t =
    let dampened_lists t =
      let rec aux index acc = function
        | [] -> acc
        | _ :: xs ->
            let without_index = List.take t index @ xs in
            aux (index + 1) (without_index :: acc) xs
      in
      aux 0 [] t
    in
    let dampened = dampened_lists t in
    List.exists dampened ~f:is_safe
end

let parse_reports ~input : Report.t list =
  String.split_lines input
  |> List.filter ~f:(fun line -> not (String.is_empty line))
  |> List.filter_map ~f:(fun line ->
         try Some (String.split ~on:' ' line |> List.map ~f:Int.of_string)
         with _ -> None)

let part_1 input =
  parse_reports ~input |> List.filter ~f:Report.is_safe |> List.length

let part_2 input =
  parse_reports ~input
  |> List.filter ~f:Report.is_safe_with_dampener
  |> List.length

let%expect_test "day 2" =
  let input =
    {|
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
|}
  in
  print_endline (Base_day.solve ~part_1 ~part_2 ~input);
  [%expect {|
    part 1: 2
    part 2: 4
    |}];
  return ()
