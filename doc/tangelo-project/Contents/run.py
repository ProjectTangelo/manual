sections = ["1. Introduction and Background", "2. System Functional Specification", "3. System Performance Requirements", "4. System Design Overview", "5. System Data Structure Specifications", "6. Module Design Specification", "7. System Verifications", "8. Conclusions", "9. Appendix", "10.Program Listings", "11. API"]
k = 1
for n in sections:
	name = n.split('.')[1].strip()
	filename = name.lower().replace(' ', '-') 
	md = "%d-%s.md" % (k, filename)

	print "\t\t- { element: chapter, number: %d, content: %s" % (
		k, md
	)

	k += 1
