package tech.wukejia;

public class Main {

    public static void main(String[] args) {
        //冒泡排序
        int target[] = {6,4,2,12,8,3,1,66,9,0};

        for(int compare_round = 0; compare_round < target.length; compare_round++){
            for(int index = 0; index < target.length-1; index++){
                if(target[index] > target[index+1]){
                    int temp = target[index];
                    target[index] = target[index+1];
                    target[index+1] = temp;
                }
            }
        }

        for(int t:target){
            System.out.print("[" + t + "]");
        }

        System.out.println("\n---");
        selectedSort();
    }

    //选择排序
    public static void selectedSort(){
        int t[] = {6,4,2,12,8,3,1,66,9,0};

        for(int round = 0; round < t.length; round++){
            int minIndx = round;
            for(int index = round+1; index < t.length; index++){
                if(t[index] < t[minIndx]){
                    minIndx = index;
                }
            }
            if(minIndx != round){
                int temp = t[round];
                t[round] = t[minIndx];
                t[minIndx] = temp;
            }
        }

        for(int i:t){
            System.out.print("[" + i + "]");
        }
    }
}
