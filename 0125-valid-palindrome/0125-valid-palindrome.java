class Solution {
    public boolean isPalindrome(String s) {
        if (s.isEmpty()) return true;
        
        int i = 0;
        int j = s.length() - 1;
        int iAscii = 0;
        int jAscii = 0;

        while (i < j) {
            iAscii = (int)s.charAt(i);
            while (!(iAscii >= 48 && iAscii <= 57) &&
                    !(iAscii >= 65 && iAscii <= 90) &&
                    !(iAscii >= 97 && iAscii <= 122) && i < s.length() - 1) {
                i++;
                iAscii = (int)s.charAt(i);
            }
            
            jAscii = (int)s.charAt(j);
            while (!(jAscii >= 48 && jAscii <= 57) &&
                    !(jAscii >= 65 && jAscii <= 90) &&
                    !(jAscii >= 97 && jAscii <= 122) && j > 0) {
                j--;
                jAscii = (int)s.charAt(j);
            }
            
            if (iAscii >= 65 && iAscii <= 90) iAscii += 32; 
            if (jAscii >= 65 && jAscii <= 90) jAscii += 32; 

            if (iAscii >= 48 && iAscii <= 57) {
                if (jAscii >= 97 && jAscii <= 122) return false;
                else if (iAscii >= 48 && iAscii <= 57) {
                    if (iAscii != jAscii) return false;     
                }
                else return false;
            }            
            else if (iAscii >= 97 && iAscii <= 122) {
                if (jAscii >= 48 && jAscii <= 57) return false;
                else if (jAscii >= 97 && jAscii <= 122) {
                    if (iAscii != jAscii) return false;
                }
                else return false;
            } 

            i++;
            j--;
        }

        return true;
    }
}