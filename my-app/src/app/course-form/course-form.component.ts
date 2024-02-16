import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ContactService } from '../contact.service';
import { CourseFormService } from '../course-form.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-course-form',
  templateUrl: './course-form.component.html',
  styleUrls: ['./course-form.component.css'],
})
export class CourseFormComponent implements OnInit {
  courseForm!: FormGroup;
  // id: number = +this.route.snapshot.params['id'];
  id!: number;

  courseData = {};

  constructor(
    private formBuilder: FormBuilder,
    // private contactService: ContactService
    private courseFormService: CourseFormService,
    private route: ActivatedRoute
  ) {}
  ngOnInit(): void {
    this.courseForm = this.formBuilder.group({
      fullname: ['', [Validators.required, Validators.maxLength(100)]],
      email: ['', [Validators.required]],
      phone: ['', [Validators.required, Validators.min(1)]],
    });
    this.id = +this.route.snapshot.params['id'];
  }
  onSubmit(): void {
    if (this.courseForm.valid) {
      // Perform data submission or API call here
      // console.log('Course ID', id);
      console.log('Form submitted with data....:', this.courseForm.value);

      // const id: number = +this.route.snapshot.params['id'];
      this.courseFormService
        // .createCourse(this.courseForm.getRawValue())
        .createCourse({
          course: this.id,
          fullname: this.courseForm.value.fullname,
          email: this.courseForm.value.email,
          phone: this.courseForm.value.phone,
        })
        .subscribe(
          (response) => {
            console.log('course form created: ');
            console.log(this.courseForm.getRawValue());

            // this.router.navigate(['thank-you']);
          },
          (error) => {
            console.error('course form creation error: ', error);
          }
        );
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
