// 프로그래머스 전화번호 목록 해쉬

import java.util.*;
import java.io.*;
class Solution {
    public boolean solution(String[] phone_book) {
        HashSet<String> set = new HashSet<>();
        for (String str : phone_book) {
            set.add(str);
        }

        for (String phone : phone_book) {
            for (int i = 1; i < phone.length(); i++) {
                String prefix = phone.substring(0, i);
                if (set.contains(prefix)) {
                    return false;
                }
            }
        }

        return true;
    }
}