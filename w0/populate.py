from pathlib import Path


def create_files():
    letters = ['A', 'B', 'C', 'D', 'E']
    numbers = ['sample', 'sample2'] + [str(i) for i in range(1, 6)]
    extensions = ['in', 'out']

    for letter in letters:
        for number in numbers:
            for ext in extensions:
                Path(f"{letter}_{number}.{ext}").touch()
        Path(f"{letter}.py").touch()
        with open(f"{letter}.sh", 'w') as f:
            for number in numbers:
                f.write(f"python3 {letter}.py < {letter}_{number}.in > {letter}_{number}.out\n")  # noqa: E501


def main():
    create_files()


if __name__ == "__main__":
    main()
