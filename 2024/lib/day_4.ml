open! Core
open Async

let label = "4"

module Grid = struct
  type t = char list list [@@deriving sexp_of]

  let of_string (input : string) : t =
    String.split_lines input |> List.map ~f:String.to_list

  let get (grid : t) (row : int) (col : int) : char option =
    List.nth grid row |> Option.bind ~f:(fun row_data -> List.nth row_data col)

  let directions =
    [ (0, 1); (1, 0); (0, -1); (-1, 0); (1, 1); (1, -1); (-1, 1); (-1, -1) ]

  let rec search_from t (row : int) (col : int) (dx : int) (dy : int)
      (word : string) (index : int) : bool =
    if index = String.length word then true
    else
      match get t row col with
      | Some c when Char.equal c word.[index] ->
          search_from t (row + dx) (col + dy) dx dy word (index + 1)
      | Some (_ : char) | None -> false

  let count_word t ~word =
    let count_from_cell row col =
      match get t row col with
      | Some 'X' ->
          List.fold directions ~init:0 ~f:(fun acc (dx, dy) ->
              if search_from t row col dx dy word 0 then acc + 1 else acc)
      | Some _ | None -> 0
    in

    List.mapi t ~f:(fun row row_data ->
        List.mapi row_data ~f:(fun col _ -> count_from_cell row col))
    |> List.concat |> List.fold ~init:0 ~f:( + )
end

let part_1 input = Grid.of_string input |> Grid.count_word ~word:"XMAS"
let part_2 _ = 1

let%expect_test "day 3" =
  let input =
    {|MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX|}
  in
  print_endline (Base_day.solve ~part_1 ~part_2 ~input);
  [%expect {|
    part 1: 18
    part 2: 1
    |}];
  return ()
