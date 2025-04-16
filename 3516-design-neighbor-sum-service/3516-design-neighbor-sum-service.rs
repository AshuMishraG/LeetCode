pub struct NeighborSum {
    grid: Vec<Vec<i32>>,
    pos: Vec<(usize, usize)>,
    n: usize,
}

impl NeighborSum {
    pub fn new(grid: Vec<Vec<i32>>) -> Self {
        let n = grid.len();
        let mut pos = vec![(0, 0); n * n];
        for i in 0..n {
            for j in 0..n {
                let value = grid[i][j] as usize;
                pos[value] = (i, j);
            }
        }
        Self { grid, pos, n }
    }
    
    pub fn adjacent_sum(&self, value: i32) -> i32 {
        const DIRS: [(isize, isize); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];
        let (r, c) = self.pos[value as usize];
        let mut sum = 0;
        for &(dr, dc) in &DIRS {
            let nr = r as isize + dr;
            let nc = c as isize + dc;
            if nr >= 0 && nr < self.n as isize && nc >= 0 && nc < self.n as isize {
                sum += self.grid[nr as usize][nc as usize];
            }
        }
        sum
    }
    
    pub fn diagonal_sum(&self, value: i32) -> i32 {
        const DIRS: [(isize, isize); 4] = [(-1, -1), (-1, 1), (1, -1), (1, 1)];
        let (r, c) = self.pos[value as usize];
        let mut sum = 0;
        for &(dr, dc) in &DIRS {
            let nr = r as isize + dr;
            let nc = c as isize + dc;
            if nr >= 0 && nr < self.n as isize && nc >= 0 && nc < self.n as isize {
                sum += self.grid[nr as usize][nc as usize];
            }
        }
        sum
    }
}
