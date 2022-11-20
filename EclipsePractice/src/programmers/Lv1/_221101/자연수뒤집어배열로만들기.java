package programmers.Lv1._221101;

public class 자연수뒤집어배열로만들기 {

	// 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
	
	class Solution {
	    public int[] solution(long n) {
	        String s = String.valueOf(n);
	        StringBuilder sb = new StringBuilder(s);
	        sb = sb.reverse();
	        
	        String[] arr = sb.toString().split("");
	        int[] answer = new int[sb.length()];
	        
	        for(int i=0;i<sb.length();i++){
	            answer[i] = Integer.parseInt(arr[i]);
	        }
	          
	        return answer;
	    }
	}
	
}
