const NUMBERS: [&str; 9] = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
];

fn parse_1(s: &str) -> u32 {
    let first = s.chars().find_map(|c| c.to_digit(10));
    let last = s.chars().rev().find_map(|c| c.to_digit(10));
    10 * first.unwrap() + last.unwrap()
}

fn check_slice(slice: &str) -> Option<u32> {
    NUMBERS.iter()
        .enumerate()
        .find(|(_, pattern)| slice.starts_with(*pattern))
        .map(|(i, _)| i as u32 + 1)
        .or_else(|| slice.chars().next().unwrap().to_digit(10))
}

fn parse_2(s: &str) -> u32 {
    let first = (0..s.len()).find_map(|i| check_slice(&s[i..]));
    let last = (0..s.len()).rev().find_map(|i| check_slice(&s[i..]));
    10 * first.unwrap() + last.unwrap()
}

fn sum_lines<F>(input: &str, parse: F) -> u32
where
    F: Fn(&str) -> u32,
{
    input
        .lines()
        .map(parse)
        .sum()
}

pub fn run(input: &str) {
    println!("{}", sum_lines(input, parse_1));
    println!("{}", sum_lines(input, parse_2));
}
