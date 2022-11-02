package programmers.Lv1._221101;

public class 짝수와홀수 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	// 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
	class Solution {
	    public String solution(int num) {
	        String answer = "";
	        if(num%2 == 0){
	            answer ="Even";
	        } else {
	            answer ="Odd";
	        }
	        
	        
	        return answer;
	    }
	}

}
