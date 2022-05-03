// 백준 2644
// 1. 부모자식들 간의 관계를 가지고 인접리스트
// 2. 방문 여부를 가지고 배열
// 3. 현재 노드에 인접한 노드를 하나씩 가져와줌
//testcase
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (p, q) => {
  //시작 촌수 p삽입
  let start = [p];
  let cnt = 0;
  while (start.length !== 0) {
    cnt += 1; //촌수 카운트
    //BFS는 최적의 경로를 구하기 때문에
    //연결된 노드를 전부 순회후 다음 노드를 순회해야한다.
    let len = start.length;

    //배열의 길이만큼 실행, 같은 촌수에 해당하는 노드 탐색,
    for (let j = 0; j < len; j++) {
      //배열에 담긴 같은 노드를 하나씩 가져와 탐색
      let tmp = start.shift();
      visited[tmp] = true; //해당 노드 방문처리
      //tmp와 연결된 노드 정보를 가져옴
      for (let z of graph[tmp]) {
        //연결된 노드가 아직 방문 처리안됬다면 탐색하지 않은 노드이다.
        if (visited[z] === false) {
          //연결된 노드가 찾는 노드(촌수)라면 리턴
          if (z === q) {
            return cnt;
          }
          //연결된 노드를 배열에 넣어줌
          start.push(z);
        }
      }
    }
  }
  //촌수가 없을시
  return -1;
};

let input = [];
let graph = [];
let  visited = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let n = Number(input.shift());
}