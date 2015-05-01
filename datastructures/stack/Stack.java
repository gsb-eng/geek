/*
 * Stack implemnetation in Java
 */

public class Stack {

    private int maxSize;
    private int top;
    private long[] stackArray;

    public Stack(int size){
        top = -1;
        maxSize = size;
        stackArray = new long[maxSize];
    }

    public void push(long value){
        stackArray[++top] = value;
    }

    public long pop(){
        return stackArray[top--];
    }

    public boolean isFull(){
        return top == maxSize -1;
    }

    public boolean isEmpty(){
        return top == -1;
    }

    public static void main(String... args){
        Stack stack = new Stack(3);
        stack.push(1);
        stack.push(2);
        System.out.println(stack.isFull());
        stack.push(3);
        System.out.println(stack.isFull());

        while(! stack.isEmpty()){
            System.out.println(stack.pop());
            System.out.println(" ");
        }
    }
}
