import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;

public class FrequencyCount {

	public static void countOccurrence(int arr[]) {
		HashMap <Integer, Integer> map = new HashMap<>();

		for (int i=0; i<arr.length; i++) {
			if (map.containsKey(arr[i]))
				map.put(arr[i], map.get(arr[i])+1);
			else
				map.put(arr[i], 1);
		}

		for (HashMap.Entry<Integer,Integer> entry: map.entrySet()) {
			System.out.println(entry.getKey() + " -> "+ entry.getValue());
		}

	}

	public static void main (String args[]) {

		Scanner sc = new Scanner(System.in);
		System.out.print("Enter the array size: ");
		int len = sc.nextInt();

		int arr[] = new int[len];

		System.out.print("Enter the array: ");

		for (int i=0; i<len; i++) {
			arr[i] = sc.nextInt();
		}

		countOccurrence(arr);

		sc.close();

	}
}