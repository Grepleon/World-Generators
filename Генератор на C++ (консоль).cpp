// здесь не только генератор, но и просто игра, если что

#include <iostream>
#include <vector>




using namespace std;



class R {
public:
    int Z; // защита
    int P; // прочность
    string Name; // имя
    R(string NName, int NZ, int NP) {
        Name = NName;
        Z = NZ;
        P = NP;
    }

    void Battle() {
        P -= 1;
    }
};


class W {
public:
    W(string NName, int NA, int NB, int NP) {
        Name = NName;
        A = NA;
        B = NB;
        P = NP;
    }


    string Name; // название
    int A; // урон
    int P; // прочность
    int B; // пробиваемость

    int Attack(int Hp, int Zht, R Arrmor) {
        if (P == 0) {
            return Hp;
        }

        if (Arrmor.P == 0) {
            Zht = 0;
        }


        if (B >= Zht) {
            Zht = 0;
        }
        else {
            Zht -= B;
        }
        if (!(P == -1)) {
            P -= 1;
        }

        
        Arrmor.Battle();
        


        return Hp - (100 - Zht) * A / 100;
    }

};

class H { // персонажи
public:
    H(string Location) {
        int Ra = rand() % 3;
        int RA = rand() % 15;
        LG = rand() % 20 + 5;
        Name_Sword = "?";
        Attack_Sword = 1;
        AZS = 10;
        P_Sword = 100;

        if (Location == "#") {  // в горах
            if (Ra == 0) { Name = "Гном"; Hp = 10 + RA; Name_Sword = "Камменый молот"; AZS += Ra; Attack_Sword += RA; }
            if (Ra == 1) { Name = "Дракон"; Hp = 25 + RA;  Name_Sword = "Пламя дракона"; AZS += Ra; Attack_Sword += RA;}
            if (Ra == 2) { Name = "Дварф"; Hp = 15 + Ra; Name_Sword = "Молот громобоя"; AZS += Ra; Attack_Sword += RA; }
        }
        if (Location == "0") {  // в земле
            if (Ra == 0) { Name = "Гоблин"; Hp = 10 + RA; Name_Sword = "Коварный нож"; AZS += Ra; Attack_Sword += RA; }
            if (Ra == 1) { Name = "Эльф"; Hp = 15 + RA; Name_Sword = "Лунный лук"; AZS += Ra; Attack_Sword += RA;}
            if (Ra == 2) { Name = "Орк"; Hp = 17 + Ra; Name_Sword = "Секира разрушения"; AZS += Ra; Attack_Sword += RA;}
        }
        if (Location == "+") {  // в земле
            if (Ra == 0) { Name = "Ведьма"; Hp = 10 + RA;  Name_Sword = "Посох теней"; AZS += Ra; Attack_Sword += RA;}
            if (Ra == 1) { Name = "Духи"; Hp = 15 + RA;  Name_Sword = "Призрачная сфера"; AZS += Ra; Attack_Sword += RA;}
            if (Ra == 2) { Name = "Болотник"; Hp = 17 + Ra;  Name_Sword = "Кувшинка яда"; AZS += Ra; Attack_Sword += RA;}
        }
        if (Location == " ") {  // в воде
            if (Ra == 0) { Name = "Русал"; Hp = 10 + RA;  Name_Sword = "Трезубец водной силы"; AZS += Ra; Attack_Sword += RA;}
            if (Ra == 1) { Name = "Тритон"; Hp = 25 + RA;  Name_Sword = "Кораловый трезубец"; AZS += Ra; Attack_Sword += RA;}
            if (Ra == 2) { Name = "Гидра"; Hp = 17 + Ra;  Name_Sword = "Отравленный клык"; AZS += Ra; Attack_Sword += RA;}
        }
    }
    string Name; // название
    int Hp; // хп
    string L; // лут/дроп
    int LG; // лут/дроп золота
    string Name_Sword;
    int Attack_Sword;
    int AZS;
    int P_Sword;

    

    

};



int main()
{
    srand(time(NULL));


    int P[100][100];
    int L[100][100];
    string O[100][100];

    int X = 100;
    int Y = 100;

    int i = 0;


    for (int x = 0; x < X; x++) {
        for (int y = 0; y < Y; y++) {
            P[x][y] = rand() % 201 - 100;
            L[x][y] = P[x][y];
        }
    }

    for (int k = 0; k < 12; k++) {
        for (int x = 0; x < X; x++) {
            for (int y = 0; y < Y; y++) {
                L[x][y] = P[x][y];
            }
        }
        for (int x = 0; x < X; x++) {
            for (int y = 0; y < Y; y++) {
                if (!(X - 1 == x || 0 == x || 0 == y || Y - 1 == y)) {
                    P[x][y] = (L[x + 1][y + 1] + L[x - 1][y + 1] + L[x + 1][y - 1] + L[x - 1][y - 1]) * 10 / 10;
                }
            }
        }
    }

    for (int x = 0; x < X; x++) {
        for (int y = 0; y < Y; y++) {
            int p = P[x][y];
            
            
            if (p > 155551130) {
                O[x][y] = "#"; // Гора
            }
            else if (p > 130) {
                O[x][y] = "0"; // Земля
            }
            else if (p > -48545330) {
                O[x][y] = "+"; // Болото
            }

            else  {
                O[x][y] = " "; // Вода
            }

            if (x == 0 || x == X - 1 || y == Y - 1 || y == 0) {
                O[x][y] = "X"; // Непроходимые стены
            }
        
        }
    
    }

    for (int x = 0; x < X; x++) {
        for (int y = 0; y < Y; y++) {
            string o = O[x][y];
            if (x != 50 || y != 50) {
                cout << o;
            }
            else {
                cout << "*";
            }
        }
        cout << "\n";
    }

    int g = 100;
    int Hp = 100;
    int Mx = 50;
    int My = 50;

    vector<W> W_Object_in_Inventri;
    vector<R> R_Object_in_Inventri;



    W Sword("Обычный меч", 5, 0, 125);
    R Arrmor("Обычная броня", 20, 125);

    setlocale(0, "Rus");
    string n = "1";
    while (n != "0") {
        string Location = O[Mx][My];
        if (Location == " ")Location = "Вода";
        if (Location == "+")Location = "Болото";
        if (Location == "#")Location = "Гора";
        if (Location == "0")Location = "Лес";
        if (Location == "X")Location = "Непроходимые горы";

        cout << "\nУ вас золота " << g << " \n";
        cout << "\nВаше оружие " << Sword.Name << " \n";
        cout << "\nВаш урон " << Sword.A << " \n";
        cout << "\nВаша бронебойность " << Sword.A << " \n";
        cout << "\nВаша прочность меча " << Sword.P << " \n";
        cout << "\nУ вас жизней " << Hp << " \n";
        cout << "\nВаша защита " << Arrmor.Name << " \n";
        cout << "\nУ вас защиты " << Arrmor.Z << " \n";
        cout << "\nВаши координаты " << Mx << " " << My << "\n";
        cout << "\nВы в '" << Location << "'\n";
        cout << "\nВаше действие? (w - вверх, a - влево, s - вниз, d - вправо, 1 - инвентарь, 2 - выбрать оружие, 3 - выбрать броню, 4 - таинственный торговец, 0 - выход): ";
        cin >> n;

        int Sx = Mx;
        int Sy = My;
        int Go = 0;

        if (n == "1") {
            for (int k = 0; k < W_Object_in_Inventri.size() - 0; k++) {
                cout << "\n" << k << ". " << W_Object_in_Inventri[k].Name << " ( прочность: " << W_Object_in_Inventri[k].P << "; урон: " << W_Object_in_Inventri[k].A << " бронебойность: " << W_Object_in_Inventri[k].B << ")\n";
            }
            for (int k = 0; k < R_Object_in_Inventri.size() - 0; k++) {
                cout << "\n" << k << ". " << R_Object_in_Inventri[k].Name << " ( прочность: " << R_Object_in_Inventri[k].P << "; защита: " << R_Object_in_Inventri[k].Z << ")\n";
            }
        }

        if (n == "2") {
            cout << "Выберите новое оружие ";
            int n1 = 0;
            cin >> n1;

           
            W Arrmor_Time = W_Object_in_Inventri[n1];

            W_Object_in_Inventri[n1] = Sword;
            Sword = Arrmor_Time;

        }

        if (n == "3") {
            cout << "Выберите новую броню ";
            int n1 = 0;
            cin >> n1;
            R Arrmor_Time = R_Object_in_Inventri[n1];

            R_Object_in_Inventri[n1] = Arrmor;
            Arrmor = Arrmor_Time;
            

        }

        if (n == "4") {
            cout << "\n1. Зелье исцеление (хп + 10) - 25 монет";
            cout << "\n2. Зелье урона (урон + 1) - 30 монет";
            cout << "\n3. Зелье защиты (защита + 1) - 5 монет";
            cout << "\n4. Зелье телепортации (от 10 до 90 по X и по Y) - 10 монет";
            cout << "\n5. Зелье прочности меча (прочность + 10) - 15 монет";

            int n2;

            cin >> n2;

            if (n2 == 1) {
                Hp += 10;
                g -= 25;
            }

            if (n2 == 2) {
                Sword.A += 1;
                g -= 30;
            }

            if (n2 == 5) {
                Sword.P += 10;
                g -= 15;
            }

            if (n2 == 4) {
                g -= 10;
                Mx = rand() % 80 + 10;
                My = rand() % 80 + 10;
            }

            if (n2 == 3) {
                Arrmor.Z += 1;
                g -= 5;
            }


        }

        if (n == "w") {
            My += 1;
            Go = 1;
        }

        if (n == "s") {
            My -= 1;
            Go = 1;
        }

        if (n == "d") {
            Mx += 1;
            Go = 1;
        }

        if (n == "a") {
            Mx -= 1;
            Go = 1;
        }

        if (Go == 1) {
            if (Location == "Непроходимые горы") { Go = 0; Mx = Sx; My = Sy; }
        }

        if (Go == 1) {
            H Mn(O[Mx][My]);
            cout << "Вы видете перед собой " << Mn.Name << " будете ли вы с ним драться? (1 - да)\n";
            int n0;
            cin >> n0;

            if (n0 == 1) {
                string NNName = "Нагрудник " + Mn.Name;
                string MNName = "Меч " + Mn.Name;
                int RRandom = rand() % 10 + 20;
                W Monstr_Sword(Mn.Name_Sword, Mn.Attack_Sword, Mn.AZS, Mn.P_Sword);
                R Monstr_Arrmor(NNName, RRandom, 100);
                while (n0 != 0 && Mn.Hp >= 0) {
                    cout << "\nПриготовьтесь к бою! Ваш ход? (0 - сбежать, 1 - атаковать)";
                    cin >> n0;
                    if (n0 == 1) {
                        
                        Mn.Hp = Sword.Attack(Mn.Hp, Monstr_Arrmor.Z, Monstr_Arrmor);
                        cout << "Вы удачно атакуете врага. У него осталось всего лишь " << Mn.Hp << " жизней. \n"<< Mn.Name <<" приготовился к атаке и наносит сокрушительный удар!" << "\n" ;
                        
                        if (Mn.Hp >= 0) {
                            

                            Hp = Monstr_Sword.Attack(Hp, Arrmor.Z, Arrmor);
                            cout << "У вас осталось " << Hp << " Хп.";

                            if (Hp <= 0) {
                                cout << "Вы умерли";
                                return 0;
                            }
                        }
                        else {
                            cout << "Умер противник... Вы получаете в инвентарь его вещи... И исцеляетесь на +5 хп невиданной энергией";
                            Hp += 5;
                            g += Mn.LG;
                            W_Object_in_Inventri.push_back(Monstr_Sword);
                            R_Object_in_Inventri.push_back(Monstr_Arrmor);


                        }

                    }
                }
            }
            else {
                Mx = Sx;
                My = Sy;
                cout << "\nВы отступаете....\n";
            }

        }
        



        //system("cls");

    }
}

