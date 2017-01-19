#Programmed by Sean Kelleher on 1/18 for Python
#This modifies the quantities of ingredients in bread recipes.

print '-- Original Recipe --'
print 'Enter the amount of Flour (cups): ',
flour = float(raw_input())
print 'Enter the amount of water (cups): ',
water = float(raw_input())
print 'Enter the amount of salt (teaspoons): ',
salt = float(raw_input())
print 'Enter the amount of yeast (teaspoons)',
yeast = float(raw_input())
print 'Enter the Loaf Adjustment Factor: ',
adjust = float(raw_input())

#Values for the modified recipe
flourMod = flour * adjust
waterMod = water * adjust
saltMod = salt * adjust
yeastMod = yeast * adjust

print ' '
print '-- Modified Recipe --'
print 'BreadFlour: %.2f cups.' % flourMod
print 'Water: %.2f cups.' % waterMod
print 'Salt: %.2f teaspoons.' % saltMod
print 'Yeast: %.2f teaspoons.' %yeastMod
print 'Happy Baking!'

#converting to grams. 
#The conversion values are based on what was shown in the assignment video
flourGrams = flourMod * 120
saltGrams = flourMod * 5
waterGrams = waterMod * 237
yeastGrams = yeastMod * 3

print ' '
print '-- Modified Recipe in Grams--'
print 'BreadFlour: %.2f g.' % flourGrams
print 'Water: %.2f g.' % waterGrams
print 'Salt: %.2f g.' % saltGrams
print 'Yeast: %.2f g.' %yeastGrams
print 'Happy Baking!'