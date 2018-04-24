//Item-Item Collaborative filtering
#include <bits/stdc++.h>
using namespace std;


float similarity_item(vector<int> itemVec1, vector<int> itemVec2){

}

int main(int argc, char const *argv[]){
	fstream infile("utility.txt");
	int userId, itemId, rating;

	vector<vector<int> > dataset;	//to read the dataset in a 2D vector.
	int userCount=-1, itemCount=-1;
	while(infile>>userId>>itemId>>rating){
		if (itemId>=500 || userId>500) {
			continue;
		}
		// cout<<userId<<" "<<itemId<<" "<<rating<<endl;
		if (userId>0 && userId<11) {
			if (itemId>0 && itemId<11) {
				cout<<userId<<" "<<itemId<<" "<<rating<<endl;
			}
		}
		userCount=max(userCount, userId);
		itemCount=max(itemCount, itemId);

		vector<int> temp;
		temp.push_back(userId);
		temp.push_back(itemId);
		temp.push_back(rating);
		dataset.push_back(temp);
	}
	cout<<"Dataset size " <<dataset.size()<<endl;
	cout<<"NO. of Users in dataset " <<userCount<<endl;
	cout<<"NO. of items in dataset " <<itemCount<<endl;

	vector<vector<int> > utilityMatrix;				//making the utility matrix out of dataset vector
	for (int i=0; i<itemCount; i++){				//utilityMatrix declaration
		vector<int> temp;
		for (int j = 0; j < userCount; j++) {
			temp.push_back(0);
		}
		utilityMatrix.push_back(temp);
	}
	for(int i=0; i<dataset.size(); i++){
		utilityMatrix[dataset[i][1]][dataset[i][0]]=dataset[i][2];
	}
	for (int i = 1; i < 10; i++) {
		for (int j = 1; j < 10; j++) {
			cout<<utilityMatrix[i][j]<<" ";
		}
		cout<<endl;
	}
	std::cout << "Hi" << '\n';
	return 0;
}
