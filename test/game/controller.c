#include <stdlib.h>
void read_inputs() { /* INSERT HERE */ }
int cop_x = 0;
int cop_y = 0;
void main() {
  {
    int prog_counter = 0;
    prog_counter = 0;
    for(;;)
      {
        if ((prog_counter == 1))
          {
            read_inputs();
            cop_x = (cop_x - 1);
            cop_y = (cop_y - 1);
            prog_counter = 1;
            continue;
          }
        if (((prog_counter == 2) && (cop_x >= 0)&& (cop_x <= 3)&& (cop_y >= 0)&& (cop_y <= 3)))
          {
            read_inputs();
            cop_x = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)) : ((cop_x == 0) ? (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= 1)&& (cop_x <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_y >= 0) && (cop_y <= 3)&& (cop_x >= 1)&& (cop_x <= 4)) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)));
            cop_y = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1))))) : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= 1)&& (cop_x <= 4)) ? (cop_y - 1) : (cop_y + 1))) : ((cop_x == 0) ? (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= 1)&& (cop_x <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_y >= 0) && (cop_y <= 3)&& (cop_x >= 1)&& (cop_x <= 4)) ? cop_y : (cop_y - 1)))) : (cop_y - 1)));
            prog_counter = ((cop_y == 0) ? ((cop_x == 0) ? 2 : 3) : 3);
            continue;
          }
        if ((prog_counter == 0))
          {
            for(;;)
              {
                if ((prog_counter == 1))
                  break;
                if (((prog_counter == 2) && (cop_x >= 0)&& (cop_x <= 3)&& (cop_y >= 0)&& (cop_y <= 3)))
                  break;
                if ((prog_counter == 0))
                  {
                    read_inputs();
                    cop_x = (cop_x - 1);
                    cop_y = (cop_y - 1);
                    prog_counter = ((cop_y == 3) ? ((cop_x >= 0) ? ((cop_x <= 3) ? ((cop_x == 3) ? 2 : 1) : 1) : 1) : 1);
                    continue;
                  }
                if (((prog_counter == 3) && (cop_y == 0)&& (cop_x == 0)))
                  {
                    read_inputs();
                    cop_x = (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1))));
                    cop_y = (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1)))));
                    prog_counter = 2;
                    continue;
                  }
                if (((prog_counter == 3) && ((cop_y == 0) || (cop_y == 1))&& ((cop_x == 0) || (cop_x == 1))))
                  {
                    read_inputs();
                    cop_x = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)) : ((cop_x == 0) ? (((cop_y == 1) && (cop_x == 1)) ? (cop_x - 1) : (((cop_x == 1) && (cop_y == (- (1)))) ? (cop_x - 1) : (((cop_y == 0) && (cop_x == 1)) ? (cop_x - 1) : (((cop_y == 1) && (cop_x == (- (1)))) ? (cop_x + 1) : (((cop_y == (- (1))) && (cop_x == (- (1)))) ? (cop_x + 1) : (((cop_y == 0) && (cop_x == (- (1)))) ? (cop_x + 1) : cop_x)))))) : (cop_x - 1)));
                    cop_y = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1))))) : (((cop_y == 1) && (cop_x == 1)) ? (cop_y - 1) : (((cop_x == 1) && (cop_y == (- (1)))) ? (cop_y + 1) : cop_y))) : ((cop_x == 0) ? (((cop_y == 1) && (cop_x == 1)) ? (cop_y - 1) : (((cop_x == 1) && (cop_y == (- (1)))) ? (cop_y + 1) : (((cop_y == 0) && (cop_x == 1)) ? cop_y : (((cop_y == 1) && (cop_x == (- (1)))) ? (cop_y - 1) : (((cop_y == (- (1))) && (cop_x == (- (1)))) ? (cop_y + 1) : (((cop_y == 0) && (cop_x == (- (1)))) ? cop_y : (cop_y - 1))))))) : (cop_y - 1)));
                    prog_counter = ((cop_y == 0) ? ((cop_x == 0) ? 2 : 3) : 3);
                    continue;
                  }
                if (((prog_counter == 3) && ((cop_y == 0) || (cop_y == 1)|| (cop_y == 2))&& ((cop_x == 0) || (cop_x == 1)|| (cop_x == 2))))
                  {
                    read_inputs();
                    cop_x = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_x - 1) : ((((cop_x == 1) || (cop_x == 2)) && ((cop_y == (- (1))) || (cop_y == 0))) ? (cop_x - 1) : ((((cop_y == 0) || (cop_y == 1)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)));
                    cop_y = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1))))) : ((((cop_y == 1) || (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_y - 1) : (cop_y + 1))) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_y - 1) : ((((cop_x == 1) || (cop_x == 2)) && ((cop_y == (- (1))) || (cop_y == 0))) ? (cop_y + 1) : ((((cop_y == 0) || (cop_y == 1)) && ((cop_x == 1) || (cop_x == 2))) ? cop_y : (cop_y - 1)))) : (cop_y - 1)));
                    prog_counter = ((cop_y == 0) ? ((cop_x == 0) ? 2 : 3) : 3);
                    continue;
                  }
                if (((prog_counter == 3) && (cop_y >= 0)&& (cop_y <= 3)&& (cop_x >= 0)&& (cop_x <= 3)))
                  {
                    read_inputs();
                    cop_x = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)|| (cop_y == 3)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_x - 1) : ((((cop_x == 1) || (cop_x == 2)|| (cop_x == 3)) && ((cop_y == (- (1))) || (cop_y == 0)|| (cop_y == 1))) ? (cop_x - 1) : ((((cop_y == 0) || (cop_y == 1)|| (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)));
                    cop_y = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1))))) : ((((cop_y == 1) || (cop_y == 2)|| (cop_y == 3)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_y - 1) : (cop_y + 1))) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)|| (cop_y == 3)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_y - 1) : ((((cop_x == 1) || (cop_x == 2)|| (cop_x == 3)) && ((cop_y == (- (1))) || (cop_y == 0)|| (cop_y == 1))) ? (cop_y + 1) : ((((cop_y == 0) || (cop_y == 1)|| (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? cop_y : (cop_y - 1)))) : (cop_y - 1)));
                    prog_counter = ((cop_y == 0) ? ((cop_x == 0) ? 2 : 3) : 3);
                    continue;
                  }
                abort();
              }
            continue;
          }
        if ((prog_counter == 1))
          {
            for(;;)
              {
                if ((prog_counter == 1))
                  break;
                if (((prog_counter == 2) && (cop_x >= 0)&& (cop_x <= 3)&& (cop_y >= 0)&& (cop_y <= 3)))
                  break;
                if ((prog_counter == 0))
                  {
                    read_inputs();
                    cop_x = (cop_x - 1);
                    cop_y = (cop_y - 1);
                    prog_counter = ((cop_y == 3) ? ((cop_x >= 0) ? ((cop_x <= 3) ? ((cop_x == 3) ? 2 : 1) : 1) : 1) : 1);
                    continue;
                  }
                if (((prog_counter == 3) && (cop_y == 0)&& (cop_x == 0)))
                  {
                    read_inputs();
                    cop_x = (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1))));
                    cop_y = (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1)))));
                    prog_counter = 2;
                    continue;
                  }
                if (((prog_counter == 3) && ((cop_y == 0) || (cop_y == 1))&& ((cop_x == 0) || (cop_x == 1))))
                  {
                    read_inputs();
                    cop_x = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)) : ((cop_x == 0) ? (((cop_y == 1) && (cop_x == 1)) ? (cop_x - 1) : (((cop_x == 1) && (cop_y == (- (1)))) ? (cop_x - 1) : (((cop_y == 0) && (cop_x == 1)) ? (cop_x - 1) : (((cop_y == 1) && (cop_x == (- (1)))) ? (cop_x + 1) : (((cop_y == (- (1))) && (cop_x == (- (1)))) ? (cop_x + 1) : (((cop_y == 0) && (cop_x == (- (1)))) ? (cop_x + 1) : cop_x)))))) : (cop_x - 1)));
                    cop_y = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1))))) : (((cop_y == 1) && (cop_x == 1)) ? (cop_y - 1) : (((cop_x == 1) && (cop_y == (- (1)))) ? (cop_y + 1) : cop_y))) : ((cop_x == 0) ? (((cop_y == 1) && (cop_x == 1)) ? (cop_y - 1) : (((cop_x == 1) && (cop_y == (- (1)))) ? (cop_y + 1) : (((cop_y == 0) && (cop_x == 1)) ? cop_y : (((cop_y == 1) && (cop_x == (- (1)))) ? (cop_y - 1) : (((cop_y == (- (1))) && (cop_x == (- (1)))) ? (cop_y + 1) : (((cop_y == 0) && (cop_x == (- (1)))) ? cop_y : (cop_y - 1))))))) : (cop_y - 1)));
                    prog_counter = ((cop_y == 0) ? ((cop_x == 0) ? 2 : 3) : 3);
                    continue;
                  }
                if (((prog_counter == 3) && ((cop_y == 0) || (cop_y == 1)|| (cop_y == 2))&& ((cop_x == 0) || (cop_x == 1)|| (cop_x == 2))))
                  {
                    read_inputs();
                    cop_x = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_x - 1) : ((((cop_x == 1) || (cop_x == 2)) && ((cop_y == (- (1))) || (cop_y == 0))) ? (cop_x - 1) : ((((cop_y == 0) || (cop_y == 1)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)));
                    cop_y = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1))))) : ((((cop_y == 1) || (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_y - 1) : (cop_y + 1))) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_y - 1) : ((((cop_x == 1) || (cop_x == 2)) && ((cop_y == (- (1))) || (cop_y == 0))) ? (cop_y + 1) : ((((cop_y == 0) || (cop_y == 1)) && ((cop_x == 1) || (cop_x == 2))) ? cop_y : (cop_y - 1)))) : (cop_y - 1)));
                    prog_counter = ((cop_y == 0) ? ((cop_x == 0) ? 2 : 3) : 3);
                    continue;
                  }
                if (((prog_counter == 3) && (cop_y >= 0)&& (cop_y <= 3)&& (cop_x >= 0)&& (cop_x <= 3)))
                  {
                    read_inputs();
                    cop_x = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)|| (cop_y == 3)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_x - 1) : ((((cop_x == 1) || (cop_x == 2)|| (cop_x == 3)) && ((cop_y == (- (1))) || (cop_y == 0)|| (cop_y == 1))) ? (cop_x - 1) : ((((cop_y == 0) || (cop_y == 1)|| (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)));
                    cop_y = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1))))) : ((((cop_y == 1) || (cop_y == 2)|| (cop_y == 3)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_y - 1) : (cop_y + 1))) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)|| (cop_y == 3)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_y - 1) : ((((cop_x == 1) || (cop_x == 2)|| (cop_x == 3)) && ((cop_y == (- (1))) || (cop_y == 0)|| (cop_y == 1))) ? (cop_y + 1) : ((((cop_y == 0) || (cop_y == 1)|| (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? cop_y : (cop_y - 1)))) : (cop_y - 1)));
                    prog_counter = ((cop_y == 0) ? ((cop_x == 0) ? 2 : 3) : 3);
                    continue;
                  }
                abort();
              }
            continue;
          }
        if (((prog_counter == 2) && (cop_x >= 0)&& (cop_x <= 3)&& (cop_y >= 0)&& (cop_y <= 3)))
          {
            for(;;)
              {
                if ((prog_counter == 1))
                  break;
                if (((prog_counter == 2) && (cop_x >= 0)&& (cop_x <= 3)&& (cop_y >= 0)&& (cop_y <= 3)))
                  break;
                if ((prog_counter == 0))
                  {
                    read_inputs();
                    cop_x = (cop_x - 1);
                    cop_y = (cop_y - 1);
                    prog_counter = ((cop_y == 3) ? ((cop_x >= 0) ? ((cop_x <= 3) ? ((cop_x == 3) ? 2 : 1) : 1) : 1) : 1);
                    continue;
                  }
                if (((prog_counter == 3) && (cop_y == 0)&& (cop_x == 0)))
                  {
                    read_inputs();
                    cop_x = (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1))));
                    cop_y = (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1)))));
                    prog_counter = 2;
                    continue;
                  }
                if (((prog_counter == 3) && ((cop_y == 0) || (cop_y == 1))&& ((cop_x == 0) || (cop_x == 1))))
                  {
                    read_inputs();
                    cop_x = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)) : ((cop_x == 0) ? (((cop_y == 1) && (cop_x == 1)) ? (cop_x - 1) : (((cop_x == 1) && (cop_y == (- (1)))) ? (cop_x - 1) : (((cop_y == 0) && (cop_x == 1)) ? (cop_x - 1) : (((cop_y == 1) && (cop_x == (- (1)))) ? (cop_x + 1) : (((cop_y == (- (1))) && (cop_x == (- (1)))) ? (cop_x + 1) : (((cop_y == 0) && (cop_x == (- (1)))) ? (cop_x + 1) : cop_x)))))) : (cop_x - 1)));
                    cop_y = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1))))) : (((cop_y == 1) && (cop_x == 1)) ? (cop_y - 1) : (((cop_x == 1) && (cop_y == (- (1)))) ? (cop_y + 1) : cop_y))) : ((cop_x == 0) ? (((cop_y == 1) && (cop_x == 1)) ? (cop_y - 1) : (((cop_x == 1) && (cop_y == (- (1)))) ? (cop_y + 1) : (((cop_y == 0) && (cop_x == 1)) ? cop_y : (((cop_y == 1) && (cop_x == (- (1)))) ? (cop_y - 1) : (((cop_y == (- (1))) && (cop_x == (- (1)))) ? (cop_y + 1) : (((cop_y == 0) && (cop_x == (- (1)))) ? cop_y : (cop_y - 1))))))) : (cop_y - 1)));
                    prog_counter = ((cop_y == 0) ? ((cop_x == 0) ? 2 : 3) : 3);
                    continue;
                  }
                if (((prog_counter == 3) && ((cop_y == 0) || (cop_y == 1)|| (cop_y == 2))&& ((cop_x == 0) || (cop_x == 1)|| (cop_x == 2))))
                  {
                    read_inputs();
                    cop_x = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_x - 1) : ((((cop_x == 1) || (cop_x == 2)) && ((cop_y == (- (1))) || (cop_y == 0))) ? (cop_x - 1) : ((((cop_y == 0) || (cop_y == 1)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)));
                    cop_y = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1))))) : ((((cop_y == 1) || (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_y - 1) : (cop_y + 1))) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_y - 1) : ((((cop_x == 1) || (cop_x == 2)) && ((cop_y == (- (1))) || (cop_y == 0))) ? (cop_y + 1) : ((((cop_y == 0) || (cop_y == 1)) && ((cop_x == 1) || (cop_x == 2))) ? cop_y : (cop_y - 1)))) : (cop_y - 1)));
                    prog_counter = ((cop_y == 0) ? ((cop_x == 0) ? 2 : 3) : 3);
                    continue;
                  }
                if (((prog_counter == 3) && (cop_y >= 0)&& (cop_y <= 3)&& (cop_x >= 0)&& (cop_x <= 3)))
                  {
                    read_inputs();
                    cop_x = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)|| (cop_y == 3)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_x - 1) : ((((cop_x == 1) || (cop_x == 2)|| (cop_x == 3)) && ((cop_y == (- (1))) || (cop_y == 0)|| (cop_y == 1))) ? (cop_x - 1) : ((((cop_y == 0) || (cop_y == 1)|| (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)));
                    cop_y = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1))))) : ((((cop_y == 1) || (cop_y == 2)|| (cop_y == 3)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_y - 1) : (cop_y + 1))) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)|| (cop_y == 3)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_y - 1) : ((((cop_x == 1) || (cop_x == 2)|| (cop_x == 3)) && ((cop_y == (- (1))) || (cop_y == 0)|| (cop_y == 1))) ? (cop_y + 1) : ((((cop_y == 0) || (cop_y == 1)|| (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? cop_y : (cop_y - 1)))) : (cop_y - 1)));
                    prog_counter = ((cop_y == 0) ? ((cop_x == 0) ? 2 : 3) : 3);
                    continue;
                  }
                abort();
              }
            continue;
          }
        if (((prog_counter == 3) && (cop_y >= 0)&& (cop_y <= 3)&& (cop_x >= 0)&& (cop_x <= 3)))
          {
            for(;;)
              {
                if ((prog_counter == 1))
                  break;
                if (((prog_counter == 2) && (cop_x >= 0)&& (cop_x <= 3)&& (cop_y >= 0)&& (cop_y <= 3)))
                  break;
                if ((prog_counter == 0))
                  {
                    read_inputs();
                    cop_x = (cop_x - 1);
                    cop_y = (cop_y - 1);
                    prog_counter = ((cop_y == 3) ? ((cop_x >= 0) ? ((cop_x <= 3) ? ((cop_x == 3) ? 2 : 1) : 1) : 1) : 1);
                    continue;
                  }
                if (((prog_counter == 3) && (cop_y == 0)&& (cop_x == 0)))
                  {
                    read_inputs();
                    cop_x = (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1))));
                    cop_y = (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1)))));
                    prog_counter = 2;
                    continue;
                  }
                if (((prog_counter == 3) && ((cop_y == 0) || (cop_y == 1))&& ((cop_x == 0) || (cop_x == 1))))
                  {
                    read_inputs();
                    cop_x = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)) : ((cop_x == 0) ? (((cop_y == 1) && (cop_x == 1)) ? (cop_x - 1) : (((cop_x == 1) && (cop_y == (- (1)))) ? (cop_x - 1) : (((cop_y == 0) && (cop_x == 1)) ? (cop_x - 1) : (((cop_y == 1) && (cop_x == (- (1)))) ? (cop_x + 1) : (((cop_y == (- (1))) && (cop_x == (- (1)))) ? (cop_x + 1) : (((cop_y == 0) && (cop_x == (- (1)))) ? (cop_x + 1) : cop_x)))))) : (cop_x - 1)));
                    cop_y = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1))))) : (((cop_y == 1) && (cop_x == 1)) ? (cop_y - 1) : (((cop_x == 1) && (cop_y == (- (1)))) ? (cop_y + 1) : cop_y))) : ((cop_x == 0) ? (((cop_y == 1) && (cop_x == 1)) ? (cop_y - 1) : (((cop_x == 1) && (cop_y == (- (1)))) ? (cop_y + 1) : (((cop_y == 0) && (cop_x == 1)) ? cop_y : (((cop_y == 1) && (cop_x == (- (1)))) ? (cop_y - 1) : (((cop_y == (- (1))) && (cop_x == (- (1)))) ? (cop_y + 1) : (((cop_y == 0) && (cop_x == (- (1)))) ? cop_y : (cop_y - 1))))))) : (cop_y - 1)));
                    prog_counter = ((cop_y == 0) ? ((cop_x == 0) ? 2 : 3) : 3);
                    continue;
                  }
                if (((prog_counter == 3) && ((cop_y == 0) || (cop_y == 1)|| (cop_y == 2))&& ((cop_x == 0) || (cop_x == 1)|| (cop_x == 2))))
                  {
                    read_inputs();
                    cop_x = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_x - 1) : ((((cop_x == 1) || (cop_x == 2)) && ((cop_y == (- (1))) || (cop_y == 0))) ? (cop_x - 1) : ((((cop_y == 0) || (cop_y == 1)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)));
                    cop_y = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1))))) : ((((cop_y == 1) || (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_y - 1) : (cop_y + 1))) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2))) ? (cop_y - 1) : ((((cop_x == 1) || (cop_x == 2)) && ((cop_y == (- (1))) || (cop_y == 0))) ? (cop_y + 1) : ((((cop_y == 0) || (cop_y == 1)) && ((cop_x == 1) || (cop_x == 2))) ? cop_y : (cop_y - 1)))) : (cop_y - 1)));
                    prog_counter = ((cop_y == 0) ? ((cop_x == 0) ? 2 : 3) : 3);
                    continue;
                  }
                if (((prog_counter == 3) && (cop_y >= 0)&& (cop_y <= 3)&& (cop_x >= 0)&& (cop_x <= 3)))
                  {
                    read_inputs();
                    cop_x = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_x - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)|| (cop_y == 3)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_x - 1) : ((((cop_x == 1) || (cop_x == 2)|| (cop_x == 3)) && ((cop_y == (- (1))) || (cop_y == 0)|| (cop_y == 1))) ? (cop_x - 1) : ((((cop_y == 0) || (cop_y == 1)|| (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_x - 1) : (cop_x + 1)))) : (cop_x - 1)));
                    cop_y = ((cop_y == 0) ? ((cop_x == 0) ? (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 1)&& (cop_y <= 4)) ? (cop_y - 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= (- (1)))&& (cop_y <= 2)) ? (cop_y + 1) : (((cop_x >= 1) && (cop_x <= 4)&& (cop_y >= 0)&& (cop_y <= 3)) ? cop_y : (((cop_y >= 1) && (cop_y <= 4)&& (cop_x >= (- (1)))&& (cop_x <= 2)) ? (cop_y - 1) : (cop_y + 1))))) : ((((cop_y == 1) || (cop_y == 2)|| (cop_y == 3)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_y - 1) : (cop_y + 1))) : ((cop_x == 0) ? ((((cop_y == 1) || (cop_y == 2)|| (cop_y == 3)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? (cop_y - 1) : ((((cop_x == 1) || (cop_x == 2)|| (cop_x == 3)) && ((cop_y == (- (1))) || (cop_y == 0)|| (cop_y == 1))) ? (cop_y + 1) : ((((cop_y == 0) || (cop_y == 1)|| (cop_y == 2)) && ((cop_x == 1) || (cop_x == 2)|| (cop_x == 3))) ? cop_y : (cop_y - 1)))) : (cop_y - 1)));
                    prog_counter = ((cop_y == 0) ? ((cop_x == 0) ? 2 : 3) : 3);
                    continue;
                  }
                abort();
              }
            continue;
          }
        abort();
      }
  }