# Sorting Algorithm Visualizer

A pygame-based visualizer for common sorting algorithms. Watch bubble sort, insertion sort, and selection sort work through an array in real time — with highlighted comparisons and a configurable speed.

## Prerequisites

- Python 3.x
- [pygame](https://www.pygame.org/)

```bash
pip install pygame
```

## Installation

```bash
git clone https://github.com/M4tn/SortingAlgorithm.git
cd SortingAlgorithm
pip install pygame
```

## Usage

```bash
python main.py
```

### Keybindings

| Key | Action |
|-----|--------|
| `R` | Shuffle the array |
| `1` | Run Selection Sort |
| `2` | Run Insertion Sort |
| `3` | Run Bubble Sort |

## Configuration

At the top of `main.py` you can tweak a few variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `total_lines` | `50` | Number of elements in the array |
| `ITER_DELAY` | `100` | Milliseconds between each step |

## Algorithms

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |

## License

MIT
