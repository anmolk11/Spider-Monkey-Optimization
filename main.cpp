#include<bits/stdc++.h>
using namespace std;

#define MAX_ITER 50
#define POPULATION_SIZE 100
#define MAX_GROUP 10
#define PR 0.2

int b1 = -10,b2 = 10;


double fitness_func(double x){
    return 5 * x - x * x + 2; // (2.5,8.25)
}

double U(int b1,int b2){
    return b1 + ((rand() + 0.0) / ( RAND_MAX / (b2-b1) ) ) ;
}

int random(int i,int j,int k){
    int r = rand() % (j - i + 1) + i;
    while(r == k){
        r = rand() % (j - i + 1) + i;
    }
    return r;
}

struct SpiderMonkey{
    private:
    int monkey_id;
    int group_id;

    double curr_pos;
    double pbest;
    double pbest_cost;

    public:

    SpiderMonkey(){
        curr_pos = b1 + U(0,1) * (b2 - b1);
    }
};

vector<vector<SpiderMonkey>> SM;

vector<SpiderMonkey> LocalLeaders;

SpiderMonkey GlobalLeader;

void LocalLeaderPhase(){
    for(int i = 0;i < SM.size();i++){
        for(int j = 0;j < SM[i].size();j++){
            if(U(0,1) >= PR){
                int r = random(0,SM[i].size() - 1,j);
                SM[i][j] = SM[i][j].curr_pos + U(0,1) * (LocalLeaders[i].curr_pos - SM[i][j].curr_pos) + U(-1,1) * (SM[i][r].curr_pos - SM[i][j].curr_pos);
            }
        }
    }
}

void GlobalLeaderPhase(){

}

void LocalLeaderDecisionPhase(){

}
    
void GlobalLeaderDecisionPhase(){
        
}

void LocalLeaderLearingPhase(){

}

void GlobalLeaderLearingPhase(){

}


int main(){

}
