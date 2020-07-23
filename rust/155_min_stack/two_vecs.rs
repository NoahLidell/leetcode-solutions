struct MinStack {
    stack: Vec<i32>,
    min_stack: Vec<i32>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    /** initialize your data structure here. */
    fn new() -> Self {
        MinStack {
            stack: Vec::new(),
            min_stack: Vec::new()}
    }
    
    fn push(&mut self, x: i32) {
        self.stack.push(x);
        if self.min_stack.len() == 0 {
            self.min_stack.push(x);
        } else if self.min_stack[self.min_stack.len() - 1] >= x {
            self.min_stack.push(x);
        }
    }
    
    fn pop(&mut self) {
        let popped = self.stack.pop();
        if popped == Some(self.min_stack[self.min_stack.len() - 1]) {
            self.min_stack.pop();
        }
    }
    
    fn top(&self) -> i32 {
        self.stack[self.stack.len() - 1]
    }
    
    fn get_min(&self) -> i32 {
        self.min_stack[self.min_stack.len() - 1]
    }
}

