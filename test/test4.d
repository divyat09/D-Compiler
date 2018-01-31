import std.stdio;

class Node(){

   private:
      int vertex;
      int edgeVertex;
      float edgeVal;

   protected:

      void initialise( int v1, int v2, float v3 ){
         this.vertex = v1; 
         this.edgeVertex = v2; 
         this.edgeVal = v3;
      }

      int EdgeWeight(){
         return edgeVal;
      }

      int VertexNum(){
         return this.vertex;
      }

      int EdgeVertexNum(){
         return this.edgeVertex;
      }

}


int main() {

   Node _Vertex1= Node();
   int v1= 5;
   int v2= 7;
   float v3= 10.4;

   _Vertex1.initialise( v1,v2,v3 );
   printf( "EdgeWeight between vertices %d and %d has value: %f", _Vertex1.VertexNum(), _Vertex1.EdgeVertexNum(),  _Vertex1.EdgeWeight() );

   return 0;

}
