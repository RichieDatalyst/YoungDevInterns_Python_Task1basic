# YoungDevInterns_Python_Task1basic
"Create a professional digital CV using Streamlit in Python. This project showcases my skills, education, projects, and contact information in an interactive and visually appealing format. Easily customize and deploy your own digital CV with this template."

You have to download streamlit ---->

pip install streamlit for windows

pip3 install streamlit for mac

In vs code terminal write above pip statement
 and on replit open shell or console and write
 this pip statement

Then import streamlit and give alias as st

and write the code

for replit before writing the code you have to create replit.nix file 
and add following packages in it.



{ pkgs }: {
    deps = [
      pkgs.tk
      pkgs.tcl
      pkgs.qhull
      pkgs.pkg-config
      pkgs.gtk3
      pkgs.gobject-introspection
      pkgs.ghostscript
      pkgs.freetype
      pkgs.ffmpeg-full
      pkgs.cairo
        pkgs.python310
        pkgs.python310Packages.pip
        pkgs.python310Packages.streamlit
    ];
}


and then write streamlit run [yourscriptname.py]
