package programmers.Lv1._221102;

public class 정수제곱근판별 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}
	
	// 문제
	// 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
	// n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
	
// answer의 변수는 long인데 i의 변수를 처음에 int라고 부여하여 틀림, int -> long으로 바꿈으로써 통과 
	class Solution {
	    public long solution(long n) {
	        long answer = 0;
	        for(long i=1;i<=n;i++){
	            if(i*i == n){
	                answer = (i+1)*(i+1);
	                break;
	            } else {
	                answer = -1 ;
	                
	            }
	        }
	        return answer;
	    }
	}
	
	
//	class Solution { 첫 시도
//	    public long solution(long n) {
//	        long answer = 0;
//	        for(int i=1;i<=n;i++){
//	            if(i*i == n){
//	                answer = (i+1)*(i+1);
//	                break;
//	            } else {
//	                answer = -1 ;
//	                
//	            }
//	        }
//	        return answer;
//	    }
//	}
	
}
