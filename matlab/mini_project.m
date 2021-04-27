%%%% RENAME from mini_project.m to (your_project_short_name).m
% Comments describing mini-project ~ 100-200 words

% Simulation parameters
%	These are values particular to the simulation 
%	that do not change later in the script

% Computed parameters (from simulation parameters)
%	These are values that do not change later in the script
%	and are calculated from formulas using the simulation parameters

% Function calls and simple calculations for:
%	data read-in
%	simulation solution 
%	visualization

% Function definitions for simulation solution & visualization
%	Each function contains help text: https://www.mathworks.com/help/matlab/matlab_prog/add-help-for-your-program.html


%%%% Feedback from reviewer:
% Does the code run without error?
% If any error occurs, can you suggest a potential fix?
 % This code errors out in line 10 due to the use of an undefined variable
 % I tried to remove % in front of the s_t declaration. The code then errored on 
 % line 13 because variable s is undefined.
 
% How understandable is the output of the code?
% Point out any parts you do not understand.
 % It would be nice to have the outputs be named without truncation.
 % Your in code comments do the job of clearing this up, but seeing words
 % in the workspace would clear up any confusion explicitly.
 % Along those lines, I wouldalso name the file something more descriptive.
 
% How readable is the code itself?
 % On a scale from 1 - 10, I give a solid 7.
 
% Say where formatting or commenting would make the code more readable
 % A comment block at the beginning of the file to describe the output of
 % the program would be a good addition.
 % Simply adding semi-colons to the end of the lines would help a lot.
 % I find my eyes being drawn to the syntax error flags. Extra spaces
 % around equal signs and operators would help smooth things out.
 
% How clearly do the code comments describe the problem it is trying to solve?
% Identify places that would benefit from a clearer comment.
 % The code coments are suitable, but most would not be needed if variables were
 % named explicitly.
 
% How clearly do the variable names relate to the concepts they concretize?
 % They could be more explicit.
 
% Point out any variables you don't recognize, and/or suggest better names.
 % s_t is the only unclear variable. I am not sure why those distances were
 % chosen.
 
% How well does the range of variables capture the problem described?
 % I am not sure where the data is coming from. For zero to 60 times, a
 % more valuable and interesting computation would come from horsepower
 % ratings.
 
% Identify extraneous regions that could be left out or important regions
% that should be included.
 % Time to travel 5 miles seems unimportant because it assumes acceleration
 % stops.
 
% How clearly do the visualizations show the solutions to the problem?
  % Visualizations were not porduced because of error in line 10.
 
% Say if there is extraneous whitespace or the co-domain or domain of the
% data should be changed or any other ways the visualizations could be more effective
 % More white space between function declarations could make code more
 % readable.
