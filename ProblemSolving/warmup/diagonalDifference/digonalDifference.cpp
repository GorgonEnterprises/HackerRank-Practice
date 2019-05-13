int diagonalDifference(vector<vector<int>> arr) {
    int sum1=0, sum2=0;
    for(int i=0;i<arr.size();i++){
        sum1+=arr[i][i];
        sum2+=arr[i][arr.size()-1-i];
    }
    return abs(sum1-sum2);
}
