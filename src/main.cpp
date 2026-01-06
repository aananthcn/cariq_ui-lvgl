#include <SDL2/SDL.h>
#include <lvgl.h>
#include <iostream>

int main(int argc, char* argv[]) {
    lv_init();

    // Initialize SDL as a window provider for LVGL
    // In LVGL v9, you use the display and input device API
    lv_display_t * disp = lv_sdl_window_create(800, 480);
    lv_indev_t * mouse = lv_sdl_mouse_create();

    // Create a simple label
    lv_obj_t * label = lv_label_create(lv_screen_active());
    lv_label_set_text(label, "Hello from C++ and SDL!");
    lv_obj_center(label);

    std::cout << "Starting UI loop..." << std::endl;

    while(1) {
        lv_timer_handler();
        SDL_Delay(5); // Small delay to save CPU
    }

    return 0;
}