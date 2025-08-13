// 標準入力のすべてを文字列として取得
const input = require("fs").readFileSync("/dev/stdin", "utf8");

// 行ごとに分割して配列に格納
const input_lines = input.split("\n");
// input_linesの中身の例: ["10", "20", "30", ""]

// 最後の空行を削除
input_lines.pop();
//----------------------

const input2 = require("fs").readFileSync("/dev/stdin", "utf8");
const input_lines2 = input2.split("\n");
input_lines2.pop();

// Nを取得
const N = parseInt(input_lines[0], 10);

// N個の整数を取得し、配列に格納
const number_list2 = [];
for (let i = 1; i <= N; i++) {
  number_list2.push(parseInt(input_lines2[i], 10));
}

// number_listの中身の例: [10, 20, 30, ...]
//--------------------------

const input3 = require("fs").readFileSync("/dev/stdin", "utf8");
const input_lines3 = input3.split("\n");
input_lines3.pop();

// 最初の行を取得
const first_line = input_lines3[0].split(" ");

// 各要素を数値に変換し、配列に格納
// number_listの中身の例: [10, 20, 30]
const number_list3 = first_line.map((str) => parseInt(str, 10));
//----------------------------

// (1) 配列操作
// sort(): 配列の要素をソートします。

// JavaScriptのsort()は、デフォルトでは文字列としてソートするため、数値のソートには工夫が必要です。

// 数値の昇順ソート: array.sort((a, b) => a - b)

// 数値の降順ソート: array.sort((a, b) => b - a)

// reverse(): 配列の要素を反転させます。

// Math.max() / Math.min(): 配列の最大値・最小値を取得します。

// スプレッド構文を使うと便利: Math.max(...array)

// reduce(): 配列の合計値を計算する際によく使います。

// array.reduce((sum, current) => sum + current, 0)

// (2) 文字列操作
// split(): 文字列を指定した区切り文字で分割し、配列にします。

// join(): 配列の要素を指定した区切り文字で結合し、文字列にします。

// trim(): 文字列の先頭と末尾にある空白文字を削除します。

// length: 文字列や配列の長さを取得します。

// 3. アプローチ方法
// 基本的な考え方はPythonと同じです。

// 入力と出力の形式を正確に確認する:

// JavaScriptでは、console.log()で出力します。

// console.log()は自動的に改行されるため、複数行の出力が必要な場合は、一行ずつconsole.log()を呼び出します。

// 最後の出力の後に余計な改行が入らないよう注意が必要です。

// テンプレートを元にコーディングする:

// まずは入力部分をテンプレート通りに書くことで、問題の核となるロジック部分に集中できます。

// JavaScriptの型に注意する:

// fs.readFileSyncで取得したデータはすべて文字列です。

// parseInt()やNumber()を使って、適切に数値型に変換することを忘れないようにしましょう。
