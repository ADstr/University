#include <stdio.h>
#include <time.h>
#include <conio.h>
#include <string.h>

void zmiana_koloru_tla( int kolor){ // 0-255
    printf("\e[48;5;%dm",kolor); //nie moze byc zadnych dodatkowych spacji
    //printf("kolor : %d\n",kolor);
};
void zmiana_koloru_tekstu( int kolor){
    printf("\e[38;5;%dm",kolor);
};
void ustaw_kursor(int wiersz, int kolumna){
    printf("\e[%d;%df", wiersz,kolumna);
};

const int black = 0;
const int green = 10;//58;
const int red = 9;
const int blue = 12;
const int white = 15;
const int grey = 7;
const int yellow = 228;
const int yellow2 = 3;
const int gold = 58;
const int purple = 10;
const int rows_number = 10;
const int cols_number = 10;
//const int sum_of_players_units = 40;

typedef struct unit_{
    char name;
    int rank;
    int move_limit;
    int amount;
}unit;

typedef struct board_tile_{
    int colour;
    char name;
    unit* tiles_unit;
}board_tile;

board_tile create_board_tile( int colour, char name){ board_tile tile = { colour, name,NULL}; return tile; };

void paint_board_tile( int colour, char name, int current_tile);

int traverse_boards( char direction, int initial_tile );

void highlight_tile( char name, int current_tile);

void init_board( board_tile* p_board, int rows_number, int cols_number, int default_colour, char default_name);
void paint_board( board_tile* board );
int travel_board( board_tile* p_board, int starting_tile);

void init_units(unit* p_units);

void paint_choose_units( unit* p_units, int colour);
void paint_choose_units_tile( int rank, char name, int amount, int colour, int current_tile);
void highlight_choose_unit_tile( unit* p_units, int current_tile);
int traverse_choose_unit(unit* p_units, int current_choose_tile, int colour);


int place_unit( unit* unit,int units_number,board_tile* p_board, int current_tile, int colour);

void highlight_move( int position, board_tile* p_board );

int main() {

    board_tile board[rows_number][cols_number];
    board[2][7]=create_board_tile(green,' ');
    board[2][8]=create_board_tile(green,' ');
    board_tile* p_board = board;
    init_board(p_board,rows_number,cols_number,green,' ');
    paint_board(p_board );

    int current_tile = 0;
    int next_tile = 0;


    ustaw_kursor(30,0);
    int unit_index = 0;
    unit units[12];
    unit* p_units = units;
    init_units(units);
    paint_choose_units(units, red);
    highlight_choose_unit_tile( units, 0);

    int red_placing_limit=40;
    int blue_placing_limit=60;
    int sum_of_players_units=1;


    int unit_number = 0;
    int units_to_place = sum_of_players_units;
    current_tile = 25;
    highlight_tile((p_board+current_tile)->name,current_tile);

    while( units_to_place > 0){
        highlight_tile((p_board+current_tile)->name,current_tile);
        unit_number=traverse_choose_unit( units, unit_number, red);
        if((units+unit_number)->amount != 0){
            current_tile=travel_board( p_board, current_tile);
            ///Czy Red umieszcza figure w swojej strefie
            if(current_tile<red_placing_limit){
                units_to_place-=place_unit( units, unit_number, p_board, current_tile,red);
                paint_board_tile((p_board+current_tile)->colour,(p_board+current_tile)->name,current_tile);
            }
            else{
                ustaw_kursor(10,60);printf("Return to your zone - beyond mountains");
                ustaw_kursor(11,60);printf("( upper half over yellow tiles ) ");
            }
        }
    }

    int amounts[12] = {1,8,5,4,4,4,3,2,1,1,1,6};
    for(int i=0;i<12;i++)(units+i)->amount=amounts[i];

    paint_choose_units( units, blue);
    unit_number = 0;
    units_to_place = sum_of_players_units;
    current_tile = 75;

    while( units_to_place > 0){
        highlight_tile((p_board+current_tile)->name,current_tile);
        unit_number=traverse_choose_unit( units, unit_number, blue);
        if((units+unit_number)->amount != 0){
            current_tile=travel_board( p_board, current_tile);
            ///Czy Blue umieszcza figure w swojej strefie
            if(current_tile>=blue_placing_limit){
                units_to_place-=place_unit( units, unit_number, p_board, current_tile,blue);
                paint_board_tile((p_board+current_tile)->colour,(p_board+current_tile)->name,current_tile);
            }
            else{
                ustaw_kursor(10,60);printf("Return to your zone - before mountains");
                ustaw_kursor(11,60);printf("( bottom half under yellow tiles ) ");
            }
        }
    }

    char caps = NULL;
    while( caps!='o'){
    current_tile=travel_board(p_board, current_tile);
    if((p_board+current_tile)->tiles_unit)
    if((p_board+current_tile)->tiles_unit->move_limit){
        unit* cur_unit=(p_board+current_tile)->tiles_unit;
        highlight_move(current_tile,p_board);

        }
    };






    p_board = NULL;
    p_units = NULL;

    return 0;
};

void highlight_move( int position, board_tile* p_board ){
 int move_position = NULL;
 paint_board_tile(yellow2,(p_board+position)->name,position);
 char moves[4]={'w','s','a','d'};

 for( int i=0; i<4; i++){
     move_position=traverse_boards(moves[i],position);
     //if(move_position->tiles_unit!=NULL || move_position->name =! 'X')
     if((p_board+move_position)->tiles_unit==NULL ||(p_board+move_position)->name != 'X'){
            highlight_tile((p_board+move_position)->name,move_position);
     }
 };
};

///ustawia pionek a w razie czego zamienia, zwraca 1 jesli przybylo pionkow na planszy
int place_unit( unit* units,int units_number, board_tile* p_board, int current_tile, int colour)
{
    int more_placed=1;
    unit* chosen_unit=units+units_number;
    board_tile* units_tile=p_board+current_tile;
    if(units_tile->tiles_unit){
        more_placed = 0;
        units_tile->tiles_unit->amount+=1;
    }
    units_tile->tiles_unit = chosen_unit;
    units_tile->name=chosen_unit->name;
    units_tile->colour=colour;
    chosen_unit->amount-=1;

    return more_placed;

};

int traverse_choose_unit(unit* p_units, int current_choose_tile, int colour){
    char direction2 = NULL;
    while( direction2 != 'p' ){
        direction2 = getch();
        paint_choose_units_tile((p_units+current_choose_tile)->rank,(p_units+current_choose_tile)->name,(p_units+current_choose_tile)->amount,colour,current_choose_tile);
        if( direction2 == 'a' && current_choose_tile > 0 )
             current_choose_tile-=1;
        else if(direction2 == 'd' && current_choose_tile < 11)
             current_choose_tile+=1;
        highlight_choose_unit_tile( p_units+current_choose_tile, current_choose_tile);
    }
    return current_choose_tile;
}

void highlight_choose_unit_tile( unit* p_units, int current_tile){
    zmiana_koloru_tekstu(black);
    paint_choose_units_tile(p_units->rank,p_units->name,p_units->amount,white,current_tile);
    zmiana_koloru_tekstu(grey);
};

void paint_choose_units( unit* p_units, int colour){
ustaw_kursor(25,0);
printf("Amount\nName\n\nRank");
for( int i=0;i<12;i++){
    paint_choose_units_tile((p_units+i)->rank,(p_units+i)->name,(p_units+i)->amount,colour,i);
};
};

void paint_choose_units_tile( int rank, char name, int amount, int colour, int current_tile){
 int current_col = 7+current_tile*7;

 ustaw_kursor(25,current_col);zmiana_koloru_tla(gold);printf("|  %d  |", amount);
 zmiana_koloru_tla(colour);
 ustaw_kursor(26,current_col);printf("|  %c  |", name);
 ustaw_kursor(27,current_col);printf("|     |");
 ustaw_kursor(28,current_col);printf("|  %d  |", rank);
 zmiana_koloru_tla(black);
 ustaw_kursor(40,current_col);
};

void init_units(unit* p_units){
     int amounts[12] = {1,8,5,4,4,4,3,2,1,1,1,6};
     char names[12]={'x','z','Z','s','p','m','M','K','G','A','F','*','@'};
     for(int i=0;i<12;i++){
        (p_units+i)->rank = i;
        (p_units+i)->move_limit=1;
        (p_units+i)->name=names[i];
        (p_units+i)->amount=amounts[i];
 };
 p_units->move_limit=100;
(p_units+10)->rank=NULL;
(p_units+10)->move_limit=NULL;
(p_units+11)->name='*';
(p_units+11)->rank=NULL;
(p_units+11)->move_limit=NULL;

};


int travel_board( board_tile* p_board, int starting_tile){
    int next_tile = 0;
    char direction = NULL;
    while( direction != 'p' ){
        direction = getch();
        paint_board_tile((p_board+starting_tile)->colour,(p_board+starting_tile)->name,starting_tile);
        next_tile = traverse_boards(direction,starting_tile);
        if((p_board+next_tile)->name != 'X')starting_tile = next_tile;
        highlight_tile((p_board+starting_tile)->name,starting_tile);
    }
    return starting_tile;
};

void paint_board_tile( int colour, char name, int current_tile){
    int cursor_row = 2 * ( current_tile/rows_number + 1 );
    int cursor_col = 5 * ( current_tile%cols_number + 1 );
    zmiana_koloru_tla(colour);
    ustaw_kursor( cursor_row, cursor_col);
    printf( "| %c |", name);
    ustaw_kursor( cursor_row+1, cursor_col);
    printf("|___|");
    zmiana_koloru_tla(black);
    ustaw_kursor(15*3,12);
};

void highlight_tile( char name, int current_tile){
    zmiana_koloru_tekstu(black);
    paint_board_tile( white,name,current_tile);
    zmiana_koloru_tekstu(grey);
};

void paint_board( board_tile* board ) {
    for( int i=0; i<rows_number*cols_number; i++)
        paint_board_tile((board+i)->colour,(board+i)->name, i);
};


void init_board( board_tile* p_board, int rows_number, int cols_number, int default_colour, char default_name){
    //init default board tiles
    for( int i=0; i<rows_number*cols_number; i++){
        (p_board+i)->colour=default_colour;
        (p_board+i)->name=default_name;
        (p_board+i)->tiles_unit=NULL;
    }
    //mark unpassable tiles in yellow and name 'X'
    for( int i=4; i<=5; i++){
        for( int j=2; j<=3; j++){
            (p_board+i*rows_number+j)->colour = yellow;
            (p_board+i*rows_number+j)->name='X';
        }
        for( int j=6; j<=7; j++){
            (p_board+i*rows_number+j)->colour = yellow;
            (p_board+i*rows_number+j)->name='X';
        }
    };
};

int traverse_boards( char direction, int initial_tile ){

    int next_tile = initial_tile;
    switch(direction){
        case 'w':
            if( initial_tile>9)next_tile=initial_tile-10;
            break;
        case 's':
            if( initial_tile<90)next_tile=initial_tile+10;
            break;
        case 'a':
            if(initial_tile%cols_number!=0 )next_tile=initial_tile-1;
            break;
        case 'd':
            if(initial_tile%cols_number!=9)next_tile=initial_tile+1;
            break;
        case 'h':
            return -1;
            break;
        case 'k':
            return 1;
            break;
        default:
           // printf("Try again to press proper keycap, maybe unpress CapsLock\n");
           // printf("Help is on right side");
           return initial_tile;
    }
    return next_tile;
};
