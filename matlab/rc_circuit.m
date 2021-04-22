%input values
voltage = 120;

capacitance_in_mufarads =132.6e-6;

resistance_in_ohms = 4;

frequency_in_hz = 60;

%ohms law fromula
voltage = current * resistance_in_ohms
resistance_in_ohms = voltage/current
current = voltage/resistance_in_ohms
power = voltage*current

%Circuit totals
total_impedence = resistor_in_ohms*capacitive reactance/sqrt(resistance_in_ohms^2 + capacitive reactance^2;
total_current = sqrt(current_across_resistor^2 + current_across_capacitor
%formulas capacitor
capacitive_reactance = 1/ (2*pi*frequency_in_hz*capacitance_in_mufarads);
current_across_capacitor = voltage/capacitive_reactance;
voltage_across_capacitor = voltage

%formulas across resistor
resistance = resisance_in_ohms
current_across_resistor = voltage/resistance

%%1. The code has a few errors that I noticed.
    %line 17 "reactance" doesnt seem to be mentioned any where else in the
    %code  so im not sure if that was a typo or if they forgot to define
    %what "reactance" is before imputting it into the equation.
    
    %line 18 seems to be missing a closing parentheses
    
    %the term voltage seems to be mentioned alot, im not sure what value or
    %equation is meant to be assigned to that term
%2. Since the code has a couple errors i cant see the output of the code.
    %Knowing this is someone else's code I dont feel comfortable editing it
    %to try to get it to work.

%3. The code is pretty readable. Since everything is spelled out it just
%takes me a little longer to process the variables in my head as to what
%they represent etc. I'm used to seeing equations represent via single
%letters.

%4. There arent very many comments, which isnt a bad thing entirely.
%5. I think the variable names relate exactly to what they represent, since
%everything is spelled out theres little to no room for interpretation.
%6. I'm not sure what problem they are trying to solve. From what I can
%gather they are working through a circuit with a preset voltage trying to
%determine the resistance, current, and total power of the circuit.
%7. There are no visualizations for this code atm.