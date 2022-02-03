import java.io.File;
import java.nio.file.FileSystems;
import java.nio.file.Paths;
import java.util.*;

public class day3_part2{

    static public void main (String[] args){

        try{
            String userDirectory = Paths.get("")
                .toAbsolutePath()
                .toString();
            File file = new File(userDirectory + "\\input.txt");
            Scanner sc = new Scanner(file);
            List<String> list = new ArrayList<String>();
            while(sc.hasNextLine()){
                list.add(sc.nextLine());
            }

            List<String> copy = list;
            
            int column = 0;
            while (list.size() > 1){
                List<String> one = new ArrayList<String>();
                List<String> zero = new ArrayList<String>();

                for (int i = 0; i < list.size(); i++){
                    if (list.get(i).charAt(column) == '1')
                        one.add(list.get(i));
                    else if (list.get(i).charAt(column) == '0')
                        zero.add(list.get(i));
                }

                if (one.size() >= zero.size()){
                    list = one;
                }
                else{
                    list = zero;
                }

                column+=1; 

            }

            System.out.println("hello world");
            int oxygen = Integer.parseInt(list.get(0), 2);
            column = 0;
            list = copy;
            while (list.size() > 1){
                List<String> one = new ArrayList<String>();
                List<String> zero = new ArrayList<String>();

                for (int i = 0; i < list.size(); i++){
                    if (list.get(i).charAt(column) == '1')
                        one.add(list.get(i));
                    else if (list.get(i).charAt(column) == '0')
                        zero.add(list.get(i));
                }

                if (one.size() < zero.size()){
                    list = one;
                }
                else{
                    list = zero;
                }

                column+=1; 

            }

            String opp = list.get(0);

            int co2 = Integer.parseInt(opp, 2);
            int total = oxygen * co2;
            System.out.println(total);

        } catch (Exception e) {
            e.getStackTrace();
        }
 
    }

}
