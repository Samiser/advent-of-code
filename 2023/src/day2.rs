#[derive(Default)]
struct Cubes {
    red: u32,
    green: u32,
    blue: u32,
}

impl Cubes {
    fn add(&self, other: &Cubes) -> Cubes {
        Cubes {
            red: self.red + other.red,
            green: self.green + other.green,
            blue: self.blue + other.blue,
        }
    }

    fn max(&self, other: &Cubes) -> Cubes {
        Cubes {
            red: std::cmp::max(self.red, other.red),
            green: std::cmp::max(self.green, other.green),
            blue: std::cmp::max(self.blue, other.blue),
        }
    }

    fn product(&self) -> u32 {
        self.red * self.green * self.blue
    }

    fn is_possible(&self) -> bool {
        self.red <= 12 && self.green <= 13 && self.blue <= 14
    }

    fn parse_segment(segment: &str) -> Cubes {
        let parts: Vec<&str> = segment.split_whitespace().collect();

        match parts[..] {
            [count, "red"] => Cubes { red: count.parse::<u32>().unwrap(), green: 0, blue: 0, },
            [count, "green"] => Cubes { red: 0, green: count.parse::<u32>().unwrap(), blue: 0, },
            [count, "blue"] => Cubes { red: 0, green: 0, blue: count.parse::<u32>().unwrap(), },
            _ => Cubes { red: 0, green: 0, blue: 0, },
        }
    }

    fn parse_line(line: &str) -> Cubes {
        line.split(", ").map(Self::parse_segment).fold(
            Cubes {
                red: 0,
                green: 0,
                blue: 0,
            },
            |acc, cubes| acc.add(&cubes),
        )
    }
}

fn parse_line(line: &str) -> Vec<Cubes> {
    line.split(": ")
        .nth(1)
        .unwrap()
        .split("; ")
        .map(Cubes::parse_line)
        .collect()
}

fn part_one(input: &str) {
    let sum: usize = input
        .lines()
        .enumerate()
        .filter(|&(_, line)| parse_line(line).iter().all(Cubes::is_possible))
        .fold(0, |acc, (index, _)| acc + index + 1);

    println!("part 1 sum: {}", sum);
}

fn min_cubes_power(game: Vec<Cubes>) -> u32 {
    game
        .into_iter()
        .fold(Cubes::default(), |acc, cubes| Cubes::max(&acc, &cubes))
        .product()
}

fn part_two(input: &str) {
    let total: u32 = input
        .lines()
        .map(parse_line)
        .map(min_cubes_power)
        .sum();

    println!("part 2 sum: {}", total);
}

pub fn run(input: &str) {
    part_one(input);
    part_two(input);
}
