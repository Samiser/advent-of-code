open! Core

module type Day = sig
  val label : string
  val part_1 : string -> int
  val part_2 : string -> int
end
