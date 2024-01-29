import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-subscription-form',
  templateUrl: './subscription-form.component.html',
  styleUrls: ['./subscription-form.component.css'],
})
export class SubscriptionFormComponent implements OnInit {
  subscriptionForm!: FormGroup;

  constructor(private formBuilder: FormBuilder, ) {}

  ngOnInit(): void {
    this.subscriptionForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.maxLength(100)]],
    });
  }
  onSubmit(): void {
    if (this.subscriptionForm.valid) {
      // Perform data submission or API call here
      console.log('Form submitted with data:', this.subscriptionForm.value);
    }
  }
}
