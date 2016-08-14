package com.longway.gradle;
class Test{
    def name;
    def id;
    Test(name,id){
        this.name = name;
        this.id = id;
    }
    void print(){
        println(name+"/"+id);
    }
}