function doGet(e) {
  var tmp = HtmlService.createTemplateFromFile('main');
  // main이라는 파일에서 템플릿을 생성하고 이를 변수 tmp에 할당
  return tmp.evaluate();
}


function getAValues(k,) {
  // 학번이 k(예:2101)인 학생의 1주일치 과목 array 반환
  var ss = SpreadsheetApp.openById("1eg3etsamY7ExSHkhIKfNX2Jsaay4Fn6Lzs59__aVxl4");
  var sheet = ss.getSheetByName("mainsheet");
  var data = sheet.getDataRange().getValues();
  //주의 : data(즉 getValues메서드) 타입 : 2차원array.
  //예: [[국어,영어,수학],[미적분,기하,확통]]
  var a = []; // 과목 담길 배열
  for (var i = 1; i < data.length; i++) 
  //note : data.length : 시트의 행 개수, data[0]: [ ,이름,월1,월2,...]
  {
    if (data[i][0] == k) { // 첫 번째 열 셀이 학번k와 일치하는 경우
      for (var j = 1; j < 36; j++) { // 두 번째 열부터 과목명을 배열에 추가(data[i][1]:학생이름))  //data[i].length
        a.push(data[i][j]);
      }
      for (var j = 36; j < data[i].length; j++ ) {
        if (['A','B','C','D','E', 'F','G'].includes(data[i][j])) {
        if (data[i][j] == 'A') {
          a.push(data[i][8]); //월7
        } 
        else if (data[i][j] == 'B') {
          a.push(data[i][4]); //월3
        }
        else if (data[i][j] == 'C') {
          a.push(data[i][19]);  //수4
        }
        else if (data[i][j] == 'D') {
          a.push(data[i][7]);  //월6
        }
        else if (data[i][j] == 'E') {
          a.push(data[i][3]);  //월2
        }
        else if (data[i][j] == 'F') {
          a.push(data[i][5]);  //월4
        }
        else if (data[i][j] == 'G') {
          a.push(data[i][22]);  //목1
        }
        
      } else {
        a.push(data[i][j]);

      }
      }
      break; // 일치하는 행을 찾았으면 반복문을 종료
    }
    
  }
  console.log(a);
  //alert(a);
  return a; // 과목명 배열을 반환
}
