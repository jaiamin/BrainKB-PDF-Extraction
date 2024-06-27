import os

# --------------

PATH = 'ground_truths/10-1101_2024-01-13-575482'
NUM_PAGES = 26

# --------------

for i in range(NUM_PAGES):
    file_path = os.path.join(PATH, f'{i+1}.txt')
    with open(file_path, 'w') as f:
        f.write('')