def count_reads(fastq_file):
    with open(fastq_file) as f:
        lines = f.readlines()
    return len(lines) // 4

if __name__ == "__main__":
    fastq = "../data/example.fastq"
    reads = count_reads(fastq)
    print(f"Number of reads: {reads}")
