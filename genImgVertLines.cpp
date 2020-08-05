/* This program generates and displays an image with n vertical lines.
    July 30 2020
*/

#include <opencv2/opencv.hpp>
using namespace cv;

int main(int argc, char const *argv[])
{
  uint width, height, n;

  std::cout<<"\n  Generates an image with n vertical white lines against a"
          <<" dark background. The values of n, image width and image height are"
          <<" read from the file, genImgVertLines.ini. \n";

  std::ifstream infile("genImgVertLines.ini");
  std::string tempstring;
  if (infile.is_open())
	{
		infile >> tempstring;
		infile >> tempstring;
		infile >> tempstring;
		// first three lines of ini file are comments
		infile >> width;
		infile >> tempstring;
		infile >> height;
		infile >> tempstring;
		infile >> n;
  }

  namedWindow("show", 0);
	moveWindow("show", 200, 0);

  Mat img(height, width, CV_64F);   // (rows,cols) or (height,width
  n++;
  for (uint y=0; y<height; y++)
  {
    for (uint p=1; p<n; p++)
    {
        img.at<double>(y,p*width/n) = 1;
    }
  }
  imshow("show", img);
  waitKey(0);
  return 0;
}
