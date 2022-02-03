import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
class main{

    public static void main(String []args){
        System.out.println("Hello World!");
        String address = "C:\\Users\\MICHAEL\\Desktop\\input2.txt";
        System.out.println(address);
        int depth = 0;
        int horizontal = 0;
        int aim = 0;
        try{
            File file = new File(
            "C:\\Users\\MICHAEL\\Desktop\\input.txt"
            );
            Scanner sc = new Scanner(file);

            while (sc.hasNextLine()){
                String line = sc.nextLine();
                String[] words = line.split(" ");
                System.out.println(words[0] + " " + words[1]);
        
                if (words[0].equals("forward")){
                    System.out.println("I was here!");
                    int num = Integer.parseInt(words[1]);
                    System.out.println(num);
                    horizontal += Integer.parseInt(words[1]);  
                    if(aim > 0){
                        depth += (aim * num);
                    }
 


                }
                else if (words[0].equals("up")){
                    aim -= Integer.parseInt(words[1]);
                    
                }
                else if (words[0].equals("down")){
                    aim += Integer.parseInt(words[1]);
                }
        
            }
        } catch (FileNotFoundException e){
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        

        int total = depth * horizontal;
        System.out.println(total);

    }
}
