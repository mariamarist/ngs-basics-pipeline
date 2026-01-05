def phred_score(char):
    return ord(char) - 33

def fastq_qc(fastq_file):
    lengths = []
    qualities = []

    with open(fastq_file) as f:
        while True:
            header = f.readline()
            if not header:
                break
            seq = f.readline().strip()
            f.readline()
            qual = f.readline().strip()

            lengths.append(len(seq))
            qualities.extend([phred_score(q) for q in qual])

    avg_length = sum(lengths) / len(lengths)
    avg_quality = sum(qualities) / len(qualities)

    return avg_length, avg_quality
