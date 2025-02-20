import java.util.*;
class Solution {
    static HashMap<String, Integer> hm = new HashMap<>();
    public int solution(String[][] clothes) {
        int answer = 1;

        for (String[] tmp : clothes) {
            String type = tmp[1];
            // 1번 방식
            // if (hm.containsKey(type)) {
            //     hm.put(type, hm.get(type) + 1);
            // } else {
            //     hm.put(type, 1);
            // }

            // 2번 방식
            // hm.putIfAbsent(type, 0);
            // hm.put(type, hm.get(type) + 1);

            // 3번 방식
            hm.put(type, hm.getOrDefault(type, 0) + 1);
        }

        for (String key : hm.keySet()) {
            answer *= (hm.get(key) + 1);
        }

        return answer - 1; // 모든 옷을 입지 않는 경우 제외
    }
}