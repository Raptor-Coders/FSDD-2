import { Component, OnInit } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  Validators,
} from '@angular/forms';

@Component({
  selector: 'app-course-form',
  templateUrl: './course-form.component.html',
  styleUrls: ['./course-form.component.css'],
})
export class CourseFormComponent implements OnInit {

  courseForm!: FormGroup;

  constructor(private formBuilder: FormBuilder) {}
  ngOnInit(): void {
    this.courseForm = this.formBuilder.group({
      name: ['', [Validators.required, Validators.maxLength(100)]],
      description: ['', [Validators.required]],
      duration: [0, [Validators.required, Validators.min(1)]],
    });
  }
  onSubmit(): void {
    if (this.courseForm.valid) {
      // Perform data submission or API call here
      console.log('Form submitted with data:', this.courseForm.value);
    }
  }
}

// @Component({
//   selector: 'app-course-form',
//   templateUrl: './course-form.component.html',
// })
// export class CourseFormComponent implements OnInit {
//   courseForm: FormGroup = this.formBuilder.group({
//     name: ['', [Validators.required, Validators.maxLength(100)]],
//     description: ['', [Validators.required]],
//     duration: [0, [Validators.required, Validators.min(1)]],
//   });

//   constructor(private formBuilder: FormBuilder) {}

//   ngOnInit(): void {}
//   onSubmit(): void {
//     if (this.courseForm.valid) {
//       // Perform data submission or API call here
//       console.log('Form submitted with data:', this.courseForm.value);
//     }
//   }
// }
