## InputHelper
This is a plugin to popup a textinput field to input Chinese text using IM (ibus, scim) in Sublime Text 2 under Linux.

New updated version 1.1.0 is:

- Fixed that the inserted string will not be selected after inputted, so that users can continue to input text.
- Added an icon for the pop-up application.

The history version 1.0.0 is seen at `https://github.com/xgenvn/InputHelper` by Anh Tu Nguyen.

## Installation
Install this repository

	cd ~/.config/sublime-text-2/Packages
	git clone https://github.com/cheng-shiwen/InputHelper.git

Or only one command

	git clone https://github.com/cheng-shiwen/InputHelper.git ~/.config/sublime-text-2/Packages/InputHelper

Or click button [**Download ZIP**][1] to download *InputHelper-master.zip* into folder *Downloads*

	cd ~/.config/sublime-text-2/Packages
	unzip ~/Downloads/InputHelper-master.zip
	mv InputHelper-master InputHelper

## Usage
- FIRST, make sure you can use your Input Method normally (test it in some textinput field)
- To insert text by using Input Method, use: Ctrl+Space
- After input text, use: Enter or Ctrl+Enter to place text to last cursor position, 
	or replace selected words on current context.
- While text is selected after input, use Ctrl+Enter again to reach new line.
- Usual key combination: Ctrl+Space -> Enter or Ctrl+Enter

## Thanks
- The original source is made by Anh Tu Nguyen, xgenvn@gmail.com.

[1]: https://github.com/cheng-shiwen/InputHelper/archive/master.zip
