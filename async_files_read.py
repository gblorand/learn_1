import asyncio


async def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = await asyncio.to_thread(file.readlines)
            return len(lines)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return 0


async def main(files):
    tasks = [count_lines(filename) for filename in files]
    line_counts = await asyncio.gather(*tasks)
    total_lines = sum(line_counts)
    print(f"Total lines in all files: {total_lines}")

if __name__ == "__main__":
    file_list = ["tests/files/file_1.txt", "tests/files/file_2.txt", "tests/files/file_3.txt"]  # List of input filenames
    asyncio.run(main(file_list))
