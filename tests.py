from mouse import Mouse;

mouse = Mouse(100, 200);
mouse.scroll(-1);
mouse.left_click();
mouse.right_click();
mouse.move(25, 50);
mouse.left_click_drag(75, 75);
mouse.release();
mouse.right_click_drag(50, 50);