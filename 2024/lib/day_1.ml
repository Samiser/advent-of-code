open! Core
open Async

let label = "1"

let parse_and_sort ~input =
  let left, right =
    String.split_lines input
    |> List.fold ~init:([], []) ~f:(fun (acc1, acc2) line ->
           match Re.split (Re.compile (Re.rep1 Re.space)) line with
           | [ left; right ] ->
               (Int.of_string left :: acc1, Int.of_string right :: acc2)
           | _ -> (acc1, acc2))
  in
  (List.sort ~compare:Int.compare left, List.sort ~compare:Int.compare right)

let part_1 input =
  let left, right = parse_and_sort ~input in
  let differences =
    List.fold2_exn left right ~init:[] ~f:(fun acc left right ->
        Int.abs (left - right) :: acc)
  in
  List.sum (module Int) differences ~f:Fn.id

let part_2 input =
  let left, right = parse_and_sort ~input in
  let similarity_scores =
    List.map left ~f:(fun left ->
        let count = List.count right ~f:(fun right -> Int.(left = right)) in
        Int.(count * left))
  in
  List.sum (module Int) similarity_scores ~f:Fn.id

let%expect_test "day 1" =
  let input = {|
3   4
4   3
2   5
1   3
3   9
3   3
|} in
  print_endline (Base_day.solve ~part_1 ~part_2 ~input);
  [%expect {|
    part 1: 11
    part 2: 31
    |}];
  return ()
