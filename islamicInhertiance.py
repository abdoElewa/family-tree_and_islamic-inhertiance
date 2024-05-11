def get_user_input():
    # استفسار عن جنس المتوفي
    died_gender = input("هل المتوفي ذكر أم أنثى؟ (ذكر/أنثى): ").lower()
    if died_gender == "ذكر":
        wife = int(input("أدخل عدد الزوجات إذا كان هناك: "))
        husband = 0
    else:
        husband = input("هل الزوج علي قيد الحياة؟ (نعم/لا): ").lower() == "نعم"
        wife = 0

    # استفسار عن قيمة الميراث وعدد الأبناء والبنات ووجود الآباء والأمهات والأجداد والجدات
    inheritance_value = float(input("الرجاء إدخال قيمة الميراث: "))
    sons = int(input("الرجاء إدخال عدد الأبناء: "))
    daughters = int(input("الرجاء إدخال عدد البنات: "))
    father = input("هل الاب علي قيد الحياة؟ (نعم/لا): ").lower() == "نعم"
    mother = input("هل الام  علي قيد الحياة؟ (نعم/لا): ").lower() == "نعم"

    if father==0:
        grandfather = input("هل الجد علي قيد الحياة؟ (نعم/لا): ").lower() == "نعم"
    else:
        grandfather=0
    if mother==0:
        grandmother = input("هل الجدة علي قيد الحياة؟ (نعم/لا): ").lower() == "نعم"
    else:
        grandmother=0
    if sons==0:
        sons_son=int(input("عدد أبناء الابن: "))
        sons_daughter=int(input("عدد بنات الابن: "))
    else :
        sons_son=0
        sons_daughter=0

    brother = 0
    sister = 0
    brother_son=0
    Mothers_brother = 0
    Mothers_sister = 0
    father_brother = 0
    father_sister = 0
    sibling_uncles = 0
    Paternal_uncles = 0
    Paternal_cousins =0
    uncle_son=0
    fb_son=0
    if sons==0 and sons_son==0 and father==0 and grandfather==0:
        brother= int(input("عدد الإخوة الأشقاء: "))
        sister= int(input("عدد الإخوات الأشقاء: "))
        if daughters==0 and sons_daughter==0:
            Mothers_brother = int(input("عدد الإخوة لأم"))
            Mothers_sister = int(input("عدد الأخوات لأم"))
        if brother==0 and (sister+daughters+sons_daughter==0):
            father_brother= int(input("عدد الإخوة من الاب"))
            father_sister= int(input("عدد الإخوات من الاب"))
        if brother == 0 and father_brother == 0:
            brother_son = int(input("عدد أبناء الإخوة الأشقاء"))
        if brother_son == 0:
            fb_son = int(input("عدد أبناء الإخوة لأب"))
        if brother_son == 0 and fb_son == 0:
            sibling_uncles = int(input(":  الأعمام الأشقاء"))
        if brother_son == 0 and fb_son == 0 and sibling_uncles == 0:
            Paternal_uncles = int(input(" الأعمام لأب"))
        if brother_son == 0 and fb_son == 0 and sibling_uncles == 0 and Paternal_uncles == 0:
            uncle_son = int(input("عدد أبناء الأعمام الأشقاء"))
        if brother_son == 0 and fb_son == 0 and sibling_uncles == 0 and Paternal_uncles == 0 and uncle_son ==0:
            Paternal_cousins = int(input("عدد أبناء الأعمام لأب"))



    return inheritance_value, sons, daughters, father, mother, grandfather, grandmother, wife, husband,sons_son,sons_daughter,brother,sister,Mothers_brother,Mothers_sister,father_brother,father_sister,sibling_uncles,Paternal_uncles,brother_son,uncle_son,fb_son,Paternal_cousins


def calculate_inheritance(inheritance_value, sons, daughters, father, mother, grandfather, grandmother, wife, husband,sons_son,sons_daughter,brother,sister,Mothers_brother,Mothers_sister,father_brother,father_sister,sibling_uncles,Paternal_uncles,brother_son,uncle_son,fb_son,Paternal_cousins):
    global total_inheritance
    total_inheritance = 0
    remain_inheritance=0
    father_inheritance = 0
    if father >0 :
        father_inheritance = inheritance_value / 6
        total_inheritance += father_inheritance

    # حساب ميراث الجد
    grandfather_inheritance = 0
    if grandfather:
        if father ==1:
            grandfather_inheritance = 0
        elif father==0 :
            grandfather_inheritance = inheritance_value / 6
        total_inheritance += grandfather_inheritance

    # حساب ميراث الأم
    mother_inheritance = 0
    if mother:
        if (sons > 0 or daughters > 0) :
            # إجراءات الشرط إذا تم تحقيقه
            mother_inheritance = inheritance_value / 6
        elif  (brother + sister + Mothers_brother + Mothers_sister > 0):
            mother_inheritance = inheritance_value / 6
        else :
            mother_inheritance = inheritance_value / 3
        total_inheritance = total_inheritance +mother_inheritance

    # حساب ميراث الجدة
    grandmother_inheritance = 0
    if grandmother:
        if mother>0:
            grandmother_inheritance = 0
        else:
            grandmother_inheritance = inheritance_value / 6
        total_inheritance += grandmother_inheritance

    # حساب ميراث الزوجة (إن وجدت)
    wife_inheritance = 0
    if wife:
        if sons > 0 or daughters >0:
            wife_inheritance = inheritance_value / 8
        else:
            wife_inheritance = inheritance_value / 4
        total_inheritance += wife_inheritance


    # حساب ميراث الزوج (إن وجد)
    husband_inheritance = 0
    if husband >0:
        if sons == 0 and daughters==0:
            husband_inheritance = inheritance_value / 2
        elif sons > 0 or daughters > 0:
            husband_inheritance = inheritance_value / 4
        else :
            husband_inheritance=0
        total_inheritance += husband_inheritance

    #son
    remain_inheritance = inheritance_value - total_inheritance
    if sons == 1 and daughters == 0:
        son_inheritance = remain_inheritance
    elif sons ==0:
        son_inheritance=0
    else:
        son_inheritance = remain_inheritance / (sons+ 0.5 *daughters)
        total_inheritance += son_inheritance*sons

    # حساب ميراث البنات
    daughter_inheritance=0
    if daughters > 0:
        if sons > 0:
            daughter_inheritance = son_inheritance * 0.5

        elif daughters==1 and sons==0:
            daughter_inheritance = inheritance_value /2
            remain_inheritance = inheritance_value - total_inheritance
        elif daughters >1 and sons==0:
            daughter_inheritance = inheritance_value *2 /3
            daughter_inheritance=daughter_inheritance / daughters
        total_inheritance += daughter_inheritance*daughters

    remain_inheritance=inheritance_value - total_inheritance
    #remain father
    if sons==0 and sons_son==0:
        if father ==1:
            father_inheritance+=remain_inheritance
            total_inheritance+=father_inheritance
        elif father==0 and grandfather==1:
            grandfather_inheritance+=remain_inheritance
            total_inheritance+=grandfather_inheritance


    #حساب ميراث ابن الابن وبنت الابن
    sons_son_inheritance=0
    sons_daughter_inheritance=0
    if sons==0 and sons_son >0:
        remain_inheritance = inheritance_value - total_inheritance
        if sons_son==1 and sons_daughter ==0:
            sons_son_inheritance=remain_inheritance
        else:
            sons_son_inheritance=remain_inheritance /(sons_son +0.5 * sons_daughter)
        total_inheritance += sons_son_inheritance * sons_son

    if sons==0 and sons_daughter >0:
        if daughters >2 and sons_son==0:
            sons_daughter_inheritance=0
        else:
            if sons_son >0:
                sons_daughter_inheritance=sons_son_inheritance *0.5
            elif sons_daughter==1 and sons_son==0 and daughters ==1:
                sons_daughter_inheritance=inheritance_value /6
            else:
                sons_daughter_inheritance= inheritance_value *3/2
        total_inheritance += sons_daughter_inheritance*sons_daughter

    #family
    Mothers_sister_inheritance = 0
    Mothers_brother_inheritance = 0
    brother_inheritance = 0
    sister_inheritance = 0
    fatherb_inheritance = 0
    fathers_inheritance = 0
    fatherb_inheritance = 0
    fb_son_inheritance = 0
    su_inheritance = 0
    pu_inheritance = 0
    us_inheritance = 0
    pc_inheritance = 0
    if sons == 0 and sons_son == 0 and father == 0 and grandfather == 0:
        third = 0
        # الاخوة لام
        if daughters == 0 and sons_daughter == 0:
            if Mothers_brother > 0 and Mothers_sister > 0:
                third = inheritance_value / 3
                Mothers_brother_inheritance = third / (Mothers_brother + Mothers_sister)
                Mothers_sister_inheritance = third / (Mothers_brother + Mothers_sister)
            elif Mothers_brother == 1 and Mothers_sister == 0:
                mothers_brother_inheritance = inheritance_value / 6

            elif Mothers_sister == 1 and Mothers_brother == 0:
                mothers_sister_inheritance = inheritance_value / 6

            total_inheritance += Mothers_brother_inheritance + Mothers_sister_inheritance


        remain_inheritance = inheritance_value - total_inheritance

        # حساب ميراث الاخ
        if brother > 0:
            if sister > 0:
                brother_inheritance = remain_inheritance / (brother + 0.5 * sister)
                sister_inheritance = brother_inheritance / 2 * sister
            else:
                remain_inheritance = inheritance_value - total_inheritance
                brother_inheritance = remain_inheritance
            total_inheritance += brother_inheritance

        if sister > 0 and brother == 0 and daughters == 0 and sons_daughter == 0:
            if sister == 1:
                sister_inheritance = inheritance_value / 2
            elif sister > 1:
                sister_inheritance = inheritance_value * 2 / 3
        elif brother == 0 and daughters > 0 or sons_daughter > 0:
            sister_inheritance = remain_inheritance
        total_inheritance += sister_inheritance

        # الاخوات من لاب
        if father_brother > 0:
            if father_sister > 0:
                fatherb_inheritance = remain_inheritance / (father_brother + 0.5 * father_sister)
                fathers_inheritance = fatherb_inheritance / 2 * father_sister
            else:
                fatherb_inheritance = remain_inheritance
        total_inheritance += fatherb_inheritance

        if father_sister > 0 and sister == 0 and daughters == 0 and sons_daughter == 0 and father_brother == 0:
            if father_sister == 1:
                fathers_inheritance = inheritance_value / 2
            elif father_sister > 1:
                fathers_inheritance = inheritance_value * 2 / 3

        elif sister_inheritance == inheritance_value / 2 and father_brother == 0:
            fathers_inheritance = inheritance_value / 6
        elif sister == 0 and brother == 0 and father_brother == 0 and (daughters > 0 or sons_daughter > 0):
            fathers_inheritance = remain_inheritance
        total_inheritance += fathers_inheritance

        total_inheritance += fathers_inheritance + fatherb_inheritance
        brothers_inheritance = 0

        if brother == 0 and father_brother == 0:
            brothers_inheritance = remain_inheritance


    if brother_son == 0:

        if fb_son > 0:
            fb_son_inheritance = remain_inheritance
            total_inheritance += remain_inheritance
    if brother_son == 0 and fb_son == 0:
        if sibling_uncles > 0:
            su_inheritance = remain_inheritance
            total_inheritance += remain_inheritance

    if brother_son == 0 and fb_son == 0 and sibling_uncles == 0:

        if Paternal_uncles > 0:
            pu_inheritance = remain_inheritance
            total_inheritance += remain_inheritance
    if brother_son == 0 and fb_son == 0 and sibling_uncles == 0 and Paternal_uncles == 0:

        if uncle_son > 0:
            us_inheritance = remain_inheritance
        else:
            if Paternal_cousins > 0:
                pc_inheritance = remain_inheritance

    total_inheritance += remain_inheritance

    return son_inheritance,father_inheritance,daughter_inheritance,mother_inheritance,wife_inheritance,grandfather_inheritance,grandmother_inheritance,husband_inheritance,daughters,sons_son_inheritance,sons_son,sons_daughter_inheritance,sons_daughter,Mothers_brother_inheritance,Mothers_sister_inheritance,brother_inheritance,sister_inheritance,fatherb_inheritance,fathers_inheritance,fb_son_inheritance,su_inheritance,pu_inheritance,us_inheritance,pc_inheritance





def print_output(son_inheritance,father_inheritance,daughter_inheritance,mother_inheritance,wife_inheritance,grandfather_inheritance,grandmother_inheritance,husband_inheritance,daughters,sons_son_inheritance,sons_son,sons_daughter_inheritance,sons_daughter,Mothers_brother_inheritance,Mothers_sister_inheritance,brother_inheritance,sister_inheritance,fatherb_inheritance,fathers_inheritance,fb_son_inheritance,su_inheritance,pu_inheritance,us_inheritance,pc_inheritance):
    if father_inheritance>0:
        print("father inheritance: ", father_inheritance)

    if wife_inheritance>0:
        print("wife inheritance: ",wife_inheritance)

    if mother_inheritance>0:
        print("mother inheritance: ",mother_inheritance)

    if son_inheritance>0:
        print("son inheritance: ",son_inheritance)

    if sons_son_inheritance>0:
        print("ابن الابن: ",sons_son_inheritance* sons_son)

    if daughter_inheritance>0:
        for i in range (daughters)  :
            print(f"daughter_inheritance {i + 1}: {daughter_inheritance }")
        print("قيمة ميراث كل البنات:", daughter_inheritance* daughters)

    if sons_daughter_inheritance >0:
        print(": بنت ابن",sons_daughter_inheritance *sons_daughter)

    if grandfather_inheritance>0:
        print("grandfather inheritance: ",grandfather_inheritance)

    if grandmother_inheritance:
        print("grandmother inheritance: ",grandmother_inheritance)

    if husband_inheritance>0:
        print("husband inheritance: ",husband_inheritance)
    if Mothers_brother_inheritance>0:
        print("  ميراث الاخوان من الام   ", Mothers_brother_inheritance)
    if Mothers_sister_inheritance>0:
        print(" مجموع ميراث الاخوات من الام  ", Mothers_sister_inheritance)
    if brother_inheritance>0:
        print("brother_inheritance :", brother_inheritance)
    if sister_inheritance>0:
        print("sister_inheritance: ", sister_inheritance)
    if fatherb_inheritance>0:
        print("مجموع ميراث الاخوان من الاب ", fatherb_inheritance)
    if fathers_inheritance>0:
        print("مجموع ميراث الاخوات من الاب", fathers_inheritance)
    if fb_son_inheritance>0:
        print(" أبناء الإخوة لأب", fb_son_inheritance)
    if su_inheritance>0:
        print(": الأعمام الأشقاء", su_inheritance)
    if pu_inheritance>0:
        print(":  الأعمام لأب", pu_inheritance)
    if us_inheritance>0:
        print("أبناء الأعمام الأشقاء", us_inheritance)
    if pc_inheritance>0:
        print("أبناء الأعمام لأب", pc_inheritance)

    print("إجمالي قيمة الميراث:", total_inheritance)



user_input = get_user_input()
calculate=calculate_inheritance(*user_input)
print_output(*calculate)