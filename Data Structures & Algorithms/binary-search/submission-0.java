class Solution {
    public int search(int[] nums, int target) {
       int len=nums.length;
       int last=len-1;
       int first=0;
       
       while(first<=last)
       {
        int mid=(first+last)/2;
        
        if(target==nums[mid]){
            return mid;}

        if (target>nums[mid]){
            first=mid+1;
    }
        else
        {
        last=mid-1;
       }
}
 return -1;
}
}