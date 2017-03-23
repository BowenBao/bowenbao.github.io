rm -r 2017
cd hexo_blog
hexo generate
cd ../
cp -r hexo_blog/public/* ./
