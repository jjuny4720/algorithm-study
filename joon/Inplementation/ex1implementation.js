function ex1(n, direction) {
  let x = 1, y = 1
  let nx = 1, ny = 1
  let plans = direction.split('')

  let dx = [0, 0, -1, 1]
  let dy = [-1, 1, 0, 0]
  let move_types = ['L', 'R', 'U', 'D']

  for (let i = 0; i < plans.length; i++) {
      for (let j = 0; j < move_types.length; j++) {
          if (plans[i] === move_types[j]) {
              nx = x + dx[j]
              ny = y + dy[j]

              if (nx < 1 || ny < 1) {
                  continue
              }
              x = nx
              y = ny
          }
      }
  }
  return `(${x},${y})`
}

console.log(ex1(5, 'R R R U D D'))